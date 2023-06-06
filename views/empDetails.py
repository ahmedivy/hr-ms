from datetime import date
from PySide6.QtCore import Slot
from sqlmodel import Session, select
from PySide6.QtWidgets import QMainWindow

from models import Employee
from core.database import engine
from views.okDialog import OkDialog
from ui.screens.empdetailswindow_ui import Ui_EmployeeDetailsWindow


class EmpDetailsWindow(QMainWindow):
    def __init__(self, emp: Employee, parent=None):
        super(EmpDetailsWindow, self).__init__()
        self.ui = Ui_EmployeeDetailsWindow()
        self.ui.setupUi(self)
        self.employee = emp
        
        self.initializeFields()
        self.ui.deleteButton.clicked.connect(self.deleteEmployee)
        
    def initializeFields(self):
        self.ui.rateField.setDecimals(2)
        self.ui.fnameField.setText(self.employee.emp_firstname)
        self.ui.lnameField.setText(self.employee.emp_lastname)
        self.ui.emailField.setText(self.employee.emp_email)
        self.ui.rateField.setValue(self.employee.emp_hourly_rate)
        self.ui.codeField.setText(str(self.employee.emp_id))
        self.ui.countryField.setText(self.employee.emp_country)
        self.ui.cityField.setText(self.employee.emp_city)
        self.ui.streetField.setText(self.employee.emp_address)
        self.ui.zipField.setText(self.employee.emp_zip)
        self.ui.phoneField.setText(self.employee.emp_phone)
        self.ui.stateField.setText(self.employee.emp_state)
        self.ui.cnicField.setText(self.employee.emp_cnic)
        self.ui.posField.setText(self.employee.emp_position)
        self.ui.hireDateField.setDate(self.employee.emp_hire_date)
        self.ui.terminationDateField.setText(
            str(self.employee.emp_termination_date) 
            if self.employee.emp_termination_date 
            else "Not Terminated"
        )
        
        self.setNonEditable()
        
    def setNonEditable(self):
        self.ui.fnameField.setReadOnly(True)
        self.ui.lnameField.setReadOnly(True)
        self.ui.emailField.setReadOnly(True)
        self.ui.rateField.setReadOnly(True)
        self.ui.codeField.setReadOnly(True)
        self.ui.countryField.setReadOnly(True)
        self.ui.cityField.setReadOnly(True)
        self.ui.streetField.setReadOnly(True)
        self.ui.zipField.setReadOnly(True)
        self.ui.phoneField.setReadOnly(True)
        self.ui.stateField.setReadOnly(True)
        self.ui.cnicField.setReadOnly(True)
        self.ui.posField.setReadOnly(True)
        self.ui.hireDateField.setReadOnly(True)
        self.ui.terminationDateField.setReadOnly(True)
        
    @Slot()
    def deleteEmployee(self):
        if self.employee.emp_termination_date:
            self.close()
        else:
            # Confirm deletion with OK/Cancel dialog
            self.dialog = OkDialog(
                message="Are you sure you want to terminate this employee?",
                title="Confirm Termination",
                parent=self
            )
            self.dialog.accepted.connect(self.terminateEmployee)
            self.dialog.rejected.connect(self.close)
            self.dialog.show()
            
            
    def terminateEmployee(self):
        # self.employee.emp_termination_date = date.today()
        self.ui.terminationDateField.setText(str(self.employee.emp_termination_date))
        
        with Session(engine) as session:
            stmt = select(Employee).where(Employee.emp_id == self.employee.emp_id)
            emp = session.exec(stmt).one()
            emp.emp_termination_date = date.today()
            session.add(emp)
            session.commit()
            
        self.close()
        
