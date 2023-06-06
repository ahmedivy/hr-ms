from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from models import *
from sqlmodel import select

from views.employeewidget import EmployeeWidget
from views.organizationwidget import OrganizationWidget
from views.attendancewidget import AttendanceWidget

from ui.screens.mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.employeeButton.clicked.connect(self.handleEmployeeMenu)
        self.ui.attendanceButton.clicked.connect(self.handleAttendanceMenu)
        self.ui.organizationButton.clicked.connect(self.handleOrganizationMenu)
    
    def handleEmployeeMenu(self):
        if not hasattr(self, 'employeeWidget'):
            self.employeeWidget = EmployeeWidget()
            self.ui.stackedWidget.addWidget(self.employeeWidget)
        self.ui.stackedWidget.setCurrentWidget(self.employeeWidget)
        
    def handleOrganizationMenu(self):
        if not hasattr(self, 'organizationWidget'):
            self.organizationWidget = OrganizationWidget()
            self.ui.stackedWidget.addWidget(self.organizationWidget)
        self.ui.stackedWidget.setCurrentWidget(self.organizationWidget)
        
    def handleAttendanceMenu(self):
        if not hasattr(self, 'attendanceWidget'):
            self.attendanceWidget = AttendanceWidget()
            self.ui.stackedWidget.addWidget(self.attendanceWidget)
        self.ui.stackedWidget.setCurrentWidget(self.attendanceWidget)

    
        
    
