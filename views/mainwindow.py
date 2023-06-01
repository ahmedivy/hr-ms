from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from models import *
from sqlmodel import select

from ui.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    
        
