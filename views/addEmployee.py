from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from ui.addemployee_ui import Ui_AddEmployeeWindow


class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super(AddEmployeeWindow, self).__init__()
        self.ui = Ui_AddEmployeeWindow()
        self.ui.setupUi(self)
        
        # Set Window Title
        self.setWindowTitle("Add Employee")
        
        self.ui.okButton.clicked.connect(self.add_employee)

    @Slot()
    def add_employee(self):
        if self.ui.fnameField.text() == "":
            self.ui.fnameField.setFocus()
            return
        if self.ui.cnicField.text() == "":
            self.ui.cnicField.setFocus()
            return
        if not self.ui.phoneField.text():
            self.ui.phoneField.setFocus()
            return
        
            
