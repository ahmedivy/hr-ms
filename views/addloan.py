from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox


from core.database import cursor
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
        stmt = "SELECT o.org_id, o.org_name FROM Organizations o"
        cursor.execute(stmt)
        organizations = cursor.fetchall()
        
        for _id, name in organizations:
            self.ui.orgField.addItem(name, _id)
            
        # Add Default Item
        self.ui.orgField.setCurrentIndex(0)
        
        # Connect the signal
        self.ui.orgField.currentIndexChanged.connect(self.handleOrgChange)
        
        
    @Slot()
    def handleOrgChange(self):
        org_id = self.ui.orgField.currentData()
        
        stmt = f"SELECT e.emp_id, e.emp_firstname + ' ' + e.emp_lastname FROM employees e WHERE e.org_id = {org_id}"
        cursor.execute(stmt)
        emps = cursor.fetchall()
            
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
        
        try:    
            if not amount or float(amount) <= 0:
                self.ui.amountField.setFocus()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Amount is not valid")
                msg.setWindowTitle("Error")
                msg.exec_()
                return 
        except:
            self.ui.amountField.setFocus()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Amount is not valid")
            msg.setWindowTitle("Error")
            msg.exec_()
            return      
        
        cursor.execute(
            f"INSERT INTO dbo.loans (emp_id, loan_amount, loan_description) VALUES ({emp_id}, {amount}, '{reason}')"
        )
        cursor.commit()
        
        self.close()
            
     