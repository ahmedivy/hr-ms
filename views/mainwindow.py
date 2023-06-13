import matplotlib.pyplot as plt
from PySide6.QtCore import Slot
from matplotlib.figure import Figure
from PySide6.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



from core.database import cursor
from views.loanwidget import LoanWidget
from views.salarywidget import SalaryWidget
from views.employeewidget import EmployeeWidget
from views.attendancewidget import AttendanceWidget
from views.organizationwidget import OrganizationWidget

from ui.screens.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.employeeButton.clicked.connect(self.handleEmployeeMenu)
        self.ui.attendanceButton.clicked.connect(self.handleAttendanceMenu)
        self.ui.organizationButton.clicked.connect(self.handleOrganizationMenu)
        self.ui.loanButton.clicked.connect(self.handleLoanMenu)
        self.ui.salariesButton.clicked.connect(self.handleSalariesMenu)
        self.ui.dashboardButton.clicked.connect(self.handleDashboardMenu)
        
        self.handleDashboardMenu()
        self.setEmployeeCount()
        
        self.setWindowTitle("HR Management System")
        
        self.ui.salaryGraph.addWidget(self.createFig())
        self.ui.empCountGraph.addWidget(self.createFig2())
        
    def setEmployeeCount(self):
        stmt = "SELECT COUNT(*) FROM employees"
        cursor.execute(stmt)
        stmt = cursor.fetchone()
        self.ui.empCountLabel.setText(str(stmt[0]))
        
    @Slot()
    def handleDashboardMenu(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.employeeScreen)
    
    @Slot()
    def handleSalariesMenu(self):
        if not hasattr(self, 'salaryWidget'):
            self.salaryWidget = SalaryWidget()
            self.ui.stackedWidget.addWidget(self.salaryWidget)
        self.ui.stackedWidget.setCurrentWidget(self.salaryWidget)
    
    @Slot()
    def handleEmployeeMenu(self):
        if not hasattr(self, 'employeeWidget'):
            self.employeeWidget = EmployeeWidget()
            self.ui.stackedWidget.addWidget(self.employeeWidget)
        self.ui.stackedWidget.setCurrentWidget(self.employeeWidget)
        
    @Slot()
    def handleOrganizationMenu(self):
        if not hasattr(self, 'organizationWidget'):
            self.organizationWidget = OrganizationWidget()
            self.ui.stackedWidget.addWidget(self.organizationWidget)
        self.ui.stackedWidget.setCurrentWidget(self.organizationWidget)
     
    @Slot()   
    def handleAttendanceMenu(self):
        if not hasattr(self, 'attendanceWidget'):
            self.attendanceWidget = AttendanceWidget()
            self.ui.stackedWidget.addWidget(self.attendanceWidget)
        self.ui.stackedWidget.setCurrentWidget(self.attendanceWidget)
        
    @Slot()
    def handleLoanMenu(self):
        if not hasattr(self, 'loanWidget'):
            self.loanWidget = LoanWidget()
            self.ui.stackedWidget.addWidget(self.loanWidget)
        self.ui.stackedWidget.setCurrentWidget(self.loanWidget)


    def createFig(self):
        def get_orgs():
            stmt = "SELECT org_id, org_name FROM organizations"
            cursor.execute(stmt)
            orgs = cursor.fetchall()
            return orgs

        def get_salaries_by_org(org_id):
            cursor.execute("EXEC [dbo].[GetSalariesLast12] @org_id = ?", org_id)
            rows = cursor.fetchall()
            return rows

        orgs = get_orgs()

        fig = Figure(figsize=(6, 4), dpi=100, facecolor='#004e89')
        ax = fig.add_subplot(111)
        colors = plt.cm.get_cmap('tab20c', len(orgs))

        for i, (_id, name) in enumerate(orgs):
            rows = get_salaries_by_org(_id)

            sal_months = []
            sal_net_amounts = []

            for ix, row in enumerate(rows, start=1):
                sal_months.append(ix)
                sal_net_amounts.append(row.total_net)

            ax.plot(sal_months, sal_net_amounts, marker='o', label=name, color=colors(i))

        ax.set_xlabel('Salaries of Last 12 Months', color='white')
        ax.set_ylabel('Net Salary', color='white')
        ax.set_title('Net Salary by Month', color='white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.grid(False)
        ax.legend(frameon=False, loc='upper left', bbox_to_anchor=(1, 1), facecolor='none', edgecolor='none', labelcolor='white')

        ax.set_facecolor('#004e89')

        ax.set_xticklabels([])

        fig.tight_layout()

        canvas = FigureCanvas(fig)

        return canvas

    
    def createFig2(self):
        def get_org_employees_count():
            stmt = "SELECT org_name, COUNT(*) AS employee_count " \
                "FROM organizations JOIN employees ON organizations.org_id = employees.org_id " \
                "GROUP BY org_name"
            cursor.execute(stmt)
            org_employees = cursor.fetchall()
            return org_employees

        org_employees = get_org_employees_count()

        org_names = [org_name for org_name, _ in org_employees]
        employee_counts = [employee_count for _, employee_count in org_employees]

        fig = Figure(figsize=(6, 4), dpi=100, facecolor='#004e89')
        ax = fig.add_subplot(111)
        colors = plt.cm.get_cmap('tab20c', len(org_employees))

        ax.bar(org_names, employee_counts, color=colors(range(len(org_employees))))

        ax.set_xlabel('Organizations', color='white')
        ax.set_ylabel('Number of Employees', color='white')
        ax.set_title('Number of Employees by Organization', color='white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(False)

        ax.set_facecolor('#004e89')

        ax.set_xticklabels([])

        ax.tick_params(colors='white')

        fig.tight_layout()

        canvas = FigureCanvas(fig)

        return canvas

