from sqlmodel import text
from PySide6.QtCore import Slot
from collections import namedtuple
from PySide6.QtWidgets import QMainWindow

from core.database import cursor
from ui.screens.addorg_ui import Ui_AddOrgWindow

Organization = namedtuple('Organization', 
    ['org_id', 'org_name', 'org_description', 'org_type', 'org_phone',
     'org_email', 'org_website', 'org_logo_url', 'org_registration_date',
     'org_address', 'org_city', 'org_state', 'org_zip', 'org_country'])


class OrgDetails(QMainWindow):
    def __init__(self, parent = None, add_org: bool = True, org_id: int = None):
        super(OrgDetails, self).__init__()
        self.parent = parent
        self.ui = Ui_AddOrgWindow()
        self.ui.setupUi(self)
        
        # Get the data from the database
        if not add_org:
            self.org = self.getOrg(org_id)
            self.populateData()
        else:
            self.org = None
            types = ["Public", "Private", "Government", "Non-Profit", "Profit"]
            
            for t in types:
                self.ui.typeField.addItem(t)
                    
        self.setWindowTitle(
            "Add New Organization" 
            if add_org else "Organization's Details"
        )
        
        self.ui.titleLabel.setText(
            "Add New Organization"
            if add_org else "Organization's Details"
        )
        
        self.ui.okButton.clicked.connect(self.handleOk)
        self.ui.cancelButton.clicked.connect(self.close)
            
    
    def getOrg(self, org_id: int):
        stmt = f'EXECUTE [dbo].[GetOrganizationDetails] {org_id}'
        cursor.execute(stmt)
        org = cursor.fetchone()
        org = Organization(*org)
        return org
            
    def populateData(self):
        self.ui.nameField.setText(self.org.org_name)
        self.ui.emailField.setText(self.org.org_email)
        self.ui.phoneField.setText(self.org.org_phone)
        self.ui.cityField.setText(self.org.org_city)
        self.ui.streetField.setText(self.org.org_address)
        self.ui.stateField.setText(self.org.org_state)
        self.ui.countryField.setText(self.org.org_country)
        self.ui.zipField.setText(self.org.org_zip)
        self.ui.websiteField.setText(self.org.org_website)
        
        types = ["Public", "Private", "Government", "Non-Profit", "Profit"]
        for t in types:
            self.ui.typeField.addItem(t)
        self.ui.typeField.setCurrentText(self.org.org_type)
        
        self.toggleEdit(True)
        
    def toggleEdit(self, state: bool):
        self.ui.nameField.setReadOnly(state)
        self.ui.emailField.setReadOnly(state)
        self.ui.phoneField.setReadOnly(state)
        self.ui.cityField.setReadOnly(state)
        self.ui.streetField.setReadOnly(state)
        self.ui.stateField.setReadOnly(state)
        self.ui.countryField.setReadOnly(state)
        self.ui.zipField.setReadOnly(state)
        self.ui.typeField.setDisabled(state)
        
        self.ui.okButton.setText("Edit" if state else "Save")
        
        types = ["Public", "Private", "Government", "Non-Profit", "Profit"]
        for t in types:
            self.ui.typeField.addItem(t)
        self.ui.typeField.setCurrentIndex(0)
        
    @Slot()
    def handleOk(self):
        if self.ui.okButton.text() == "Edit":
            self.toggleEdit(False)
        else:
            self.saveData()
            self.close()
            
    def saveData(self):
        if self.org is None:
            self.createOrg()
        else:
            self.updateOrg()
            
    def createOrg(self):
            proc_call = "EXEC CreateOrganization ?, ?, ?, ?, ?, ?, ?, ?, ?"
    
            # Extract the values from the UI fields
            name = self.ui.nameField.text()
            email = self.ui.emailField.text()
            phone = self.ui.phoneField.text()
            city = self.ui.cityField.text()
            address = self.ui.streetField.text()
            state = self.ui.stateField.text()
            country = self.ui.countryField.text()
            _zip = self.ui.zipField.text()
            _type = self.ui.typeField.currentText()
            
            
#               @name NVARCHAR(50),
#   @email NVARCHAR(50),
#   @website NVARCHAR(50),
#   @type NVARCHAR(50),
#   @phone NVARCHAR(20),
#   @city NVARCHAR(100),
#   @address NVARCHAR(100),
#   @state NVARCHAR(50),
#   @country NVARCHAR(50),
#   @zip NVARCHAR(20)
            # Execute the stored procedure
            cursor.execute(proc_call, (name, email, _type, phone, city, address, state, country, _zip))
            cursor.commit()
            self.close()
            self.parent.tableRefresh()
            
    def updateOrg(self):
            proc_call = "EXEC UpdateOrganization ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
            
            print('Updating organization')
            
            # Extract the values from the UI fields
            _id = self.org.org_id
            name = self.ui.nameField.text()
            email = self.ui.emailField.text()
            website = self.ui.websiteField.text()
            phone = self.ui.phoneField.text()
            city = self.ui.cityField.text()
            address = self.ui.streetField.text()
            state = self.ui.stateField.text()
            country = self.ui.countryField.text()
            _zip = self.ui.zipField.text()
            _type = self.ui.typeField.currentText()
            
            # Execute the stored procedure
            cursor.execute(proc_call, (_id, name, email, website, _type, phone, city, address, state, country, _zip))
            cursor.commit()
            
            self.close()
            self.parent.tableRefresh()

        
                
