from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from ui.loginwindow_ui import Ui_LoginWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.on_login)

    @Slot()
    def on_login(self):
        ...
