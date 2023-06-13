from typing import List
from collections import namedtuple
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import cursor
from ui.static.css import tableViewStyles
from ui.widgets.attendance_ui import Ui_AttendanceWidget

from views.addattendance import AddAttendanceWindow
from views.attendancedetails import AttendanceDetailsWindow

   
Attendance = namedtuple("Attendance", ["atd_id", "atd_date", "present_employees", "absent_employees"])


class AtendanceTableModel(QAbstractTableModel):
    
    def __init__(self, attendance: List[Attendance]):
        super(AtendanceTableModel, self).__init__()
        
        self.attendance = attendance
        self.filterAttendance = attendance
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
            attendance = self.filterAttendance[index.row()]
            if index.column() == 0:
                return attendance.atd_id
            elif index.column() == 1:
                return str(attendance.atd_date)
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
        
        self.populateOrganizationComboBox()
        self.loadAttendance()
        self.ui.tableView.setStyleSheet(tableViewStyles)
        
        self.ui.addButton.clicked.connect(self.handleAddAttendance)
        self.ui.orgField.currentIndexChanged.connect(self.loadAttendance)
        

        
    def addButtons(self):
        for ix in range(self.model.rowCount()):
            button = QPushButton("Details", self)
            button.clicked.connect(self.handleClick)
            self.ui.tableView.setIndexWidget(self.ui.tableView.model().index(ix, 4), button)
            
    def populateOrganizationComboBox(self):
        stmt = "SELECT org_id, org_name FROM Organizations"
        cursor.execute(stmt)
        for org_id, org_name in cursor.fetchall():
            self.ui.orgField.addItem(org_name, org_id)
            
        self.ui.orgField.setCurrentIndex(0)
        
    def handleClick(self):
        button = self.sender()
        index = self.ui.tableView.indexAt(button.pos())
        attendance_id = self.model.attendance[index.row()][0]
        self.detailsWindow = AttendanceDetailsWindow(attendance_id)
        self.detailsWindow.show()
        
        
        
    def loadAttendance(self):
        org_id = self.ui.orgField.currentData()
        stmt = f"EXEC GetAttendanceDetails {org_id}"
        cursor.execute(stmt)
        attds = cursor.fetchall()
        attds = [Attendance(*attd) for attd in attds]
        self.model = AtendanceTableModel(attds)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addButtons()
    
    @Slot()
    def handleAddAttendance(self):
        # Open Add Attendance Window
        self.addAttendanceWindow = AddAttendanceWindow(self)
        self.addAttendanceWindow.show()
        
    
