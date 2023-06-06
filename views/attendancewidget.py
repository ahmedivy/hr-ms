from typing import Optional
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from models import Employee
from core.database import engine
from ui.widgets.attendance_ui import Ui_AttendanceWidget

from views.addattendance import AddAttendanceWindow


class AtendanceTableModel(QAbstractTableModel):
    
    def __init__(self, attendance: list):
        super(AtendanceTableModel, self).__init__()
        
        self.attendance = attendance
        self.header = [
            "Attendance ID",
            "Attendace Date",
            "Present Employees",
            "Absent Employees",
            "Actions"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.attendance)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            attendance = self.attendance[index.row()]
            if index.column() == 0:
                return attendance.attendance_id
            elif index.column() == 1:
                return attendance.attendance_date
            elif index.column() == 2:
                return attendance.present_employees
            elif index.column() == 3:
                return attendance.absent_employees
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]


class AttendanceWidget(QWidget):
    def __init__(self):
        super(AttendanceWidget, self).__init__()
        self.ui = Ui_AttendanceWidget()
        self.ui.setupUi(self)
        
        self.loadAttendance()
        self.addButtons()
        
        self.ui.addButton.clicked.connect(self.handleAddAttendance)
        
    def addButtons(self):
        # for ix in range(self.model.rowCount()):
        #     button = QPushButton("Details", self)
        #     button.clicked.connect(self.handleClick)
        #     self.ui.tableView.setIndexWidget(self.ui.tableView.model().index(ix, 5), button)
        ...
        
    def handleClick(self):
        ...
        
    def loadAttendance(self):
        ...
        
    @Slot()
    def handleAddAttendance(self):
        # Open Add Attendance Window
        self.addAttendanceWindow = AddAttendanceWindow()
        self.addAttendanceWindow.show()
        
    
