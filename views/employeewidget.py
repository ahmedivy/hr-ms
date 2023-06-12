from collections import namedtuple
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import cursor
from ui.static.css import tableViewStyles
from views.empDetails import EmpDetailsWindow
from views.addEmployee import AddEmployeeWindow
from ui.widgets.employeeWidget_ui import Ui_EmployeeWidget


Employee = namedtuple('Employee', [
    'emp_id', 'emp_firstname', 'emp_lastname', 'emp_hourly_rate', 'emp_email'
])

class EmployeeTableModel(QAbstractTableModel):
    
    def __init__(self, employees: list[Employee]):
        super(EmployeeTableModel, self).__init__()
        self.employees = employees
        self.filtered_employees = employees
        self.header = ["Code", "First Name", "Last Name", "Hourly Rate", "Email", "Actions"]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.filtered_employees)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            employee = self.filtered_employees[index.row()]
            if index.column() == 0:
                return employee.emp_id
            elif index.column() == 1:
                return employee.emp_firstname
            elif index.column() == 2:
                return employee.emp_lastname
            elif index.column() == 3:
                return int(employee.emp_hourly_rate)
            elif index.column() == 4:
                return employee.emp_email
        
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]

class EmployeeWidget(QWidget):
    def __init__(self):
        super(EmployeeWidget, self).__init__()
        self.ui = Ui_EmployeeWidget()
        self.ui.setupUi(self)
        
        self.populate_fields()
        self.loadEmployees()
        self.addButtons()
        self.ui.addButton.clicked.connect(self.addEmployee)
        self.ui.tableView.setStyleSheet(tableViewStyles)
        
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.searchField.returnPressed.connect(self.search)
        self.ui.orgField.currentIndexChanged.connect(self.loadEmployees)
        
    @Slot()
    def addEmployee(self):
        self.addWindow = AddEmployeeWindow(self)
        self.addWindow.show()    
    
    def addButtons(self):
        for ix in range(self.model.rowCount()):
            button = QPushButton("Details", self)
            button.clicked.connect(self.handleClick)
            self.ui.tableView.setIndexWidget(self.ui.tableView.model().index(ix, 5), button)
            
            
    def loadEmployees(self):        
        stmt = f"SELECT emp_id, emp_firstname, emp_lastname, emp_hourly_rate, emp_email FROM employees" \
                f" WHERE org_id = {self.ui.orgField.currentData()}"
                
        cursor.execute(stmt)
        employees = cursor.fetchall()
        employees = [Employee(*emp) for emp in employees]
        
        
        self.model = EmployeeTableModel(employees)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addButtons()
        
    def populate_fields(self):
        stmt = "SELECT org_id, org_name FROM organizations"
        cursor.execute(stmt)
        
        for _id, name in cursor.fetchall():
            self.ui.orgField.addItem(name, _id)
            
        self.ui.orgField.setCurrentIndex(0)
            
    @Slot()
    def handleClick(self):
        button = self.sender()
        index = self.ui.tableView.indexAt(button.pos())
        emp = self.model.filtered_employees[index.row()]
        self.empDetails = EmpDetailsWindow(emp.emp_id)
        self.empDetails.show()
        
        # Refresh the table view
        self.empDetails.ui.deleteButton.clicked.connect(self.loadEmployees)
                   
    @Slot()
    def search(self):
        if not self.ui.searchField.text():
            self.model.filtered_employees = self.model.employees
        else:
            self.model.filtered_employees = self.filterEmployees(self.ui.searchField.text().lower())
        self.model.layoutChanged.emit()
        self.addButtons()
    
    def filterEmployees(self, search: str):
        name = lambda emp: f"{emp.emp_firstname} {emp.emp_lastname}".lower()
        mask = lambda emp: search in name(emp).lower()
        return [emp for emp in self.model.employees if mask(emp)]
        