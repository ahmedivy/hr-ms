from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from core.database import cursor
from ui.screens.addemployee_ui import Ui_AddEmployeeWindow


class AddEmployeeWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AddEmployeeWindow, self).__init__()
        self.ui = Ui_AddEmployeeWindow()
        self.ui.setupUi(self)
        
        self.parent = parent
        
        self.populateOrganizationComboBox()
        
        # Set Window Title
        self.setWindowTitle("Add Employee")
        
        self.ui.confirmButton.clicked.connect(self.addEmployee)
        self.ui.cancelButton.clicked.connect(self.close)

    @Slot()
    def addEmployee(self):
        # Get the field values from self.ui
        org_id = self.ui.orgField.currentData()
        firstname = self.ui.fnameField.text()
        lastname = self.ui.lnameField.text()
        email = self.ui.emailField.text()
        phone = self.ui.phoneField.text()
        address = self.ui.streetField.text()
        city = self.ui.cityField.text()
        state = self.ui.stateField.text()
        zip_code = self.ui.zipField.text()
        country = self.ui.countryField.text()
        position = self.ui.posField.text()
        hourly_rate = self.ui.rateField.value()

        # Validate the fields
        if not firstname or not email or not phone or not position or not hourly_rate:
            return

        # Insert the data into the SQL Server employee table
        sql = '''
            INSERT INTO [dbo].[employees] (
                [org_id],
                [emp_firstname],
                [emp_lastname],
                [emp_email],
                [emp_phone],
                [emp_address],
                [emp_city],
                [emp_state],
                [emp_zip],
                [emp_country],
                [emp_position],
                [emp_hourly_rate]
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        params = (
            org_id,
            firstname,
            lastname,
            email,
            phone,
            address,
            city,
            state,
            zip_code,
            country,
            position,
            hourly_rate
        )

        cursor.execute(sql, params)
        cursor.commit()   
        
        self.close()
        self.parent.loadData()  
    
    def populateOrganizationComboBox(self):
        stmt = "SELECT org_id, org_name FROM Organizations"
        cursor.execute(stmt)
        for org_id, org_name in cursor.fetchall():
            self.ui.orgField.addItem(org_name, org_id)
            
        self.ui.orgField.setCurrentIndex(0)  
