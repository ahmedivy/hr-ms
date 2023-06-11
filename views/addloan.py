from sqlmodel import text
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow


from core.database import engine, cursor
from ui.screens.addloan_ui import Ui_AddLoanWindow


class AddLoanWindow(QMainWindow):
    def __init__(self):
        super(AddLoanWindow, self).__init__()
        self.ui = Ui_AddLoanWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Add New Loan")
        
        self.ui.okButton.clicked.connect(self.handleOk)
        self.ui.cancelButton.clicked.connect(self.close)
        
        self.populateOrganization()
        
    def populateOrganization(self):
        with engine.connect() as conn:
            stmt = text(
                "SELECT o.org_id, o.org_name FROM Organizations o"
            )
            result = conn.execute(stmt)
            organizations = result.fetchall()
        
        for org in organizations:
            self.ui.orgField.addItem(org.org_name, org.org_id)
            
        # Add Default Item
        self.ui.orgField.setCurrentIndex(0)
        
        # Connect the signal
        self.ui.orgField.currentIndexChanged.connect(self.handleOrgChange)
        
    @Slot()
    def handleOrgChange(self):
        org_id = self.ui.orgField.currentData()
        
        with engine.connect() as conn:
            stmt = text(f"SELECT e.emp_id, e.emp_firstname + ' ' + e.emp_lastname FROM employees e WHERE e.org_id = {org_id}")
            result = conn.execute(stmt)
            emps = result.fetchall()
            
        self.ui.empField.clear()
        for emp in emps:
            self.ui.empField.addItem(emp[1], emp[0])
            
        # Add Default Item
        self.ui.empField.setCurrentIndex(0)
        
    @Slot()
    def handleOk(self):
        emp_id = self.ui.empField.currentData()
        amount = self.ui.amountField.text()
        reason = self.ui.reasonField.text()
        
        if not amount:
            self.ui.amountField.setFocus()
            return
        print(emp_id, amount, reason)
        
        stmt = cursor.execute(
            f"INSERT INTO dbo.loans (emp_id, loan_amount, loan_description) VALUES ({emp_id}, {amount}, '{reason}')"
        )
        cursor.commit()
        
                
        
        self.close()
            
     