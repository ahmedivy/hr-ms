from PySide6.QtWidgets import QMainWindow, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

from core.database import cursor
from ui.static.css import tableViewStyles
from ui.screens.attendancedetails_ui import Ui_AttendanceDetailsWindow

class AttendanceDetailsModel(QAbstractTableModel):
    
    def __init__(self, attendance: list):
        super(AttendanceDetailsModel, self).__init__()
        
        self.attendance = attendance
        self.header = [
            "Employee ID",
            "Employee Name",
            "Time In",
            "Time Out",
            "Work Hours"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.attendance)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            id, name, time_in, time_out, work_hours = self.attendance[index.row()]
            if index.column() == 0:
                return id
            elif index.column() == 1:
                return name
            elif index.column() == 2:
                return str(time_in)
            elif index.column() == 3:
                return str(time_out)
            elif index.column() == 4:
                return work_hours
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]
            

class AttendanceDetailsWindow(QMainWindow):
    def __init__(self, attendance_id: int):
        super(AttendanceDetailsWindow, self).__init__()
        self.ui = Ui_AttendanceDetailsWindow()
        self.ui.setupUi(self)
        
        self.attendance_id = attendance_id
        self.ui.tableView.setStyleSheet(tableViewStyles)

        self.populateDateField()
        self.loadAttendanceDetails()
        
    def loadAttendanceDetails(self):
        stmt = f"EXEC GetAttendanceDetailByID {self.attendance_id}"
        cursor.execute(stmt)
        attendance = cursor.fetchall()
        self.model = AttendanceDetailsModel(attendance)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    def populateDateField(self):
        stmt = f"SELECT atd_date FROM Attendance WHERE atd_id = {self.attendance_id}"
        cursor.execute(stmt)
        date = cursor.fetchone()[0]
        label = f'Attendance for {date}'
        self.ui.dateField.setText(label)
        self.ui.dateField.setReadOnly(True)
        
        
        