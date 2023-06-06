from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from models import *
from sqlmodel import select

from ui.screens.loginwindow_ui import Ui_LoginWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        

    @Slot()
    def on_login(self):
        stmt = select(Employee).where(Employee.username == self.ui.username.text())
