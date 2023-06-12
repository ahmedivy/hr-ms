from collections import namedtuple
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import cursor
from views.addorg import OrgDetails
from ui.static.css import tableViewStyles
from ui.widgets.organizationWidget_ui import Ui_OrganizationWidget


Organization = namedtuple('Organization',[
    'org_id', 'org_name', 'org_phone', 'org_email', 'org_location', 'total_employees'
])
                          

class OrganizationModel(QAbstractTableModel):
    def __init__(self, orgs: list):
        super(OrganizationModel, self).__init__()
        self.orgs = orgs
        self.headers = [
            "Name",
            "Email",
            "Phone",
            "Location",
            "Total Employees",
            "Actions"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.orgs)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.headers)
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]
            
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            org = self.orgs[index.row()]
            if index.column() == 0:
                return org.org_name
            elif index.column() == 1:
                return org.org_email
            elif index.column() == 2:
                return org.org_phone
            elif index.column() == 3:
                return org.org_location
            elif index.column() == 4:
                return org.total_employees


class OrganizationWidget(QWidget):
    def __init__(self):
        super(OrganizationWidget, self).__init__()
        self.ui = Ui_OrganizationWidget()
        self.ui.setupUi(self)
        
        # Populate the table
        self.loadData()
        
        self.ui.tableView.setStyleSheet(tableViewStyles)
        
        self.ui.newButton.clicked.connect(self.handleNew)
        
    def loadData(self):
        
        # Get the data from the database    
        stmt = "EXEC GetOrganizations"
        cursor.execute(stmt)
        orgs = cursor.fetchall()
        orgs = [Organization(*org) for org in orgs]
        self.model = OrganizationModel(orgs)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addButtons()
        
        
    def addButtons(self):
        for ix in range(self.model.rowCount()):
            button = QPushButton("Details", self)
            button.clicked.connect(self.handleClick)
            self.ui.tableView.setIndexWidget(self.model.index(ix, 5), button)
          
    @Slot()
    def handleClick(self):
        button = self.sender()
        index = self.ui.tableView.indexAt(button.pos())
        org_id = self.model.orgs[index.row()].org_id
        self.orgDetails = OrgDetails(parent = self, add_org = False, org_id = org_id)
        self.orgDetails.show()
        
    @Slot()
    def handleNew(self):
        self.addOrgWindow = OrgDetails()
        self.addOrgWindow.show(parent = self)
        
    def tableRefresh(self):
        self.loadData()
          