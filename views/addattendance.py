import pandas as pd
from sqlmodel import text
from datetime import date, timedelta, datetime

from PySide6.QtCore import Slot
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog, QHeaderView, QPushButton

from core.database import engine

from ui.screens.addattendance_ui import Ui_AddAttendanceWindow


class AttendanceDetailsModel(QAbstractTableModel):
    
    def __init__(self, attendance: list):
        super(AttendanceDetailsModel, self).__init__()
        
        self.attendances: list = attendance
        self.header: list = [
            "Employee ID",
            "Employee Name",
            "In Time",
            "Out Time",
            "Total Hours",
            "Actions"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.attendances)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            attendance = self.attendances[index.row()]
            if index.column() == 0:
                return attendance['emp_id']
            elif index.column() == 1:
                return attendance['emp_name']
            elif index.column() == 2:
                return attendance['time_in'].strftime("%H:%M")
            elif index.column() == 3:
                return attendance['time_out'].strftime("%H:%M")
            elif index.column() == 4:
                # Assuming attendance['time_in'] and attendance['time_out'] are datetime.time objects
                time_in = datetime.combine(date.today(), attendance['time_in'])
                time_out = datetime.combine(date.today(), attendance['time_out'])
                # Calculate the difference in hours
                hours = (time_out - time_in).total_seconds() / 3600
                return f"{hours:.2f}"
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]

class AddAttendanceWindow(QMainWindow):

    def __init__(self):
        super(AddAttendanceWindow, self).__init__()
        self.ui = Ui_AddAttendanceWindow()
        self.ui.setupUi(self)
        
        self.ui.uploadButton.clicked.connect(self.upload_attendance)
        
        today = date.today().strftime("%Y-%m-%d") + " (Today)"
        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d") + " (Yesterday)"
        self.ui.dateField.addItems([today, yesterday])
            
        self.ui.confirmButton.hide()
        self.ui.confirmButton.clicked.connect(self.confirm_attendance)
        
    def addButtons(self):
        for ix in range(self.model.rowCount()):
            button = QPushButton("Details", self)
            button.clicked.connect(self.handleClick)
            self.ui.tableView.setIndexWidget(self.model.index(ix, 5), button)
            
    @Slot()
    def handleClick(self):
        ...
        
    @Slot()
    def confirm_attendance(self):
        att_date = self.ui.dateField.currentText().split(" ")[0]
        
        # TODO: Check if attendance already exists for this date
                
        with engine.begin() as conn:
            stmt = text("EXECUTE InsertAttendance :att_date, :org_id")
            stmt = stmt.bindparams(att_date=att_date, org_id=106)
            conn.execute(stmt)
            
            # Get the attendance id
            stmt = text("SELECT atd_id FROM Attendance WHERE atd_date = :atd_date AND org_id = :org_id")
            stmt = stmt.bindparams(atd_date=att_date, org_id=106)
            att_id = conn.execute(stmt).first()[0]
            
            # Insert attendance details
            for ix in range(self.model.rowCount()):
                emp_id = self.model.data(self.model.index(ix, 0), Qt.DisplayRole)
                time_in = self.model.data(self.model.index(ix, 2), Qt.DisplayRole)
                time_out = self.model.data(self.model.index(ix, 3), Qt.DisplayRole)
                
                stmt = text("EXECUTE InsertAttendanceDetails :atd_id, :emp_id, :time_in, :time_out")
                stmt = stmt.bindparams(atd_id=att_id, emp_id=emp_id, time_in=time_in, time_out=time_out)
                conn.execute(stmt)
        
    @Slot()
    def upload_attendance(self):
        # Open File Dialog
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Attendance File",
            "",
            "CSV Files (*.csv)"
        )
        
        # Check if file is selected
        if file_name:
            # Insert
            df = pd.read_csv(file_name)
            df['time_in'] = pd.to_datetime(df['time_in'], format='%H:%M').dt.time
            df['time_out'] = pd.to_datetime(df['time_out'], format='%H:%M').dt.time
            self.model = AttendanceDetailsModel(df.to_dict("records"))
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.addButtons()
            
            self.ui.confirmButton.show()
        
            
            
