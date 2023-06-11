from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import cursor
from views.addsalary import AddSalaryWindow
from views.salarydetails import SalaryDetailWindow
from ui.widgets.salarywidget_ui import Ui_SalaryWidget


class SalaryTableModel(QAbstractTableModel):
    
    def __init__(self, salaries: list):
        super(SalaryTableModel, self).__init__()
        self.salaries = salaries
        self.header = [
            "Sal ID",
            "Month and Year",
            "Total Gross Salary",
            "Total Deductions",
            "Total Net Salary",
            "Actions"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.salaries)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            _id, month_year, gross, deductions, net = self.salaries[index.row()]
        
            if index.column() == 0:
                return _id
            elif index.column() == 1:
                return month_year
            elif index.column() == 2:
                return str(gross)
            elif index.column() == 3:
                return str(deductions)
            elif index.column() == 4:
                return str(net)
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]
            


class SalaryWidget(QWidget):
    def __init__(self):
        super(SalaryWidget, self).__init__()
        self.ui = Ui_SalaryWidget()
        self.ui.setupUi(self)
        
        self.populate_fields()
        self.loadData()
        
        self.ui.orgField.currentIndexChanged.connect(self.loadData)
        self.ui.generateSalaryButton.clicked.connect(self.handleNew)
        
    def loadData(self):
        _id = self.ui.orgField.currentData()
        stmt = f"EXEC GetSalariesByOrg {_id}"
        cursor.execute(stmt)
        
        salaries = cursor.fetchall()
        self.model = SalaryTableModel(salaries)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.addButton()
        
    
    def addButton(self):
        for ix in range(self.model.rowCount()):
            button = QPushButton("View")
            button.clicked.connect(self.handleDetails)
            self.ui.tableView.setIndexWidget(self.model.index(ix, 5), button)
        
    def handleDetails(self):
        button = self.sender()
        index = self.ui.tableView.indexAt(button.pos())
        salary = self.model.salaries[index.row()]
        self.salaryDetailWindow = SalaryDetailWindow(salary)
        self.salaryDetailWindow.show()       
        
    @Slot()
    def handleNew(self):
        self.addSalaryWindow = AddSalaryWindow()
        self.addSalaryWindow.show()
        
    def populate_fields(self):
        stmt = "SELECT org_id, org_name FROM organizations"
        cursor.execute(stmt)
        
        for id, name in cursor.fetchall():
            self.ui.orgField.addItem(name, id)
            
        self.ui.orgField.setCurrentIndex(0)
