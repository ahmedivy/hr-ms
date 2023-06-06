from sqlmodel import text
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from core.database import engine
from ui.screens.addorg_ui import Ui_AddOrgWindow


class OrgDetails(QMainWindow):
    def __init__(self, add_org: bool = True, org_id: int = None):
        super(OrgDetails, self).__init__()
        self.ui = Ui_AddOrgWindow()
        self.ui.setupUi(self)
        
        # Get the data from the database
        if not add_org:
            self.org = self.getOrg(org_id)
            self.populateData()
        else:
            self.org = None
        
        self.setWindowTitle(
            "Add New Organization" 
            if add_org else "Organization's Details"
        )
        
        self.ui.titleLabel.setText(
            "Add New Organization"
            if add_org else "Organization's Details"
        )
        
        self.ui.okButton.clicked.connect(self.handleOk)
            
    
    def getOrg(self, org_id: int):
        with engine.connect() as conn:
            stmt = text("EXECUTE [dbo].[GetOrganizationDetails] @id = :org_id")
            stmt = stmt.bindparams(org_id=org_id)
            org = conn.execute(stmt).first()
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
        with engine.connect() as conn:
            stmt = text("EXECUTE [dbo].[CreateOrganization] "
                "@name = :name, "
                "@email = :email,"
                "@phone = :phone,"
                "@city = :city,"
                "@address = :address,"
                "@state = :state,"
                "@country = :country,"
                "@zip = :zip,"
                "@type = :type"
            )
            stmt = stmt.bindparams(
                name=self.ui.nameField.text(),
                email=self.ui.emailField.text(),
                phone=self.ui.phoneField.text(),
                city=self.ui.cityField.text(),
                address=self.ui.streetField.text(),
                state=self.ui.stateField.text(),
                country=self.ui.countryField.text(),
                zip=self.ui.zipField.text(),
                type=self.ui.typeField.currentText()
            )
            conn.execute(stmt)
            
    def updateOrg(self):
        with engine.connect() as conn:
            stmt = text("EXECUTE [dbo].[UpdateOrganization] "
                "@id = :id, "
                "@name = :name, "
                "@email = :email,"
                "@website = :website,"
                "@phone = :phone,"
                "@city = :city,"
                "@address = :address,"
                "@state = :state,"
                "@country = :country,"
                "@zip = :zip,"
                "@type = :type"
            )
            stmt = stmt.bindparams(
                id=self.org.org_id,
                name=self.ui.nameField.text(),
                email=self.ui.emailField.text(),
                website=self.ui.websiteField.text(),
                phone=self.ui.phoneField.text(),
                city=self.ui.cityField.text(),
                address=self.ui.streetField.text(),
                state=self.ui.stateField.text(),
                country=self.ui.countryField.text(),
                zip=self.ui.zipField.text(),
                type=self.ui.typeField.currentText()
            )
            conn.execute(stmt)
