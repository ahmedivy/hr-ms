from datetime import date
from calendar import month_name
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox

from core.database import cursor
from ui.screens.addsalary_ui import Ui_AddSalaryWindow


class AddSalaryWindow(QMainWindow):
    
    def __init__(self):
        super(AddSalaryWindow, self).__init__()
        self.ui = Ui_AddSalaryWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Add Salary")
        
        self.populate_fields()
        
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.confirmButton.clicked.connect(self.add_salary)
        
        
    @Slot()
    def add_salary(self):
        # Check if the salary for the month and year already exists
        _id = self.ui.orgField.currentData()
        year = self.ui.yearField.currentText()
        month = self.ui.monthField.currentText()
        stmt = f"SELECT * FROM salary WHERE sal_month = '{month}' AND sal_year = '{year}' AND org_id = {_id}"
        cursor.execute(stmt)
        
        if cursor.fetchone():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Salary for the month and year already exists")
            msg.setWindowTitle("Error")
            # Set size of the message box
            # msg.setStyleSheet("QLabel{min-width:500 px; font-size: 24px;} QPushButton{ width:250px; font-size: 18px; }");
            msg.exec_()
            return
        
        
        
        
            
            
        
        
        
    def populate_fields(self):
        months = month_name[1:]
        years = [str(year) for year in range(2020, date.today().year + 1)]
        self.ui.yearField.addItems(years)
        self.ui.monthField.addItems(months)
        
        stmt = "SELECT org_id, org_name FROM organizations"
        cursor.execute(stmt)
        
        for id, name in cursor.fetchall():
            self.ui.orgField.addItem(name, id)
        
        