from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from models import *

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
        
        self.setWindowTitle("HR Management System")
    
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

    
        
    
