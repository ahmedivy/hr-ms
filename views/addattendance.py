import pandas as pd
from PySide6.QtCore import Slot
from datetime import date, timedelta, datetime
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog, QHeaderView, QMessageBox


from core.database import cursor
from ui.static.css import tableViewStyles
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
                time_in = datetime.combine(date.today(), attendance['time_in'])
                time_out = datetime.combine(date.today(), attendance['time_out'])
                hours = (time_out - time_in).total_seconds() / 3600
                return f"{hours:.2f}"
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]

class AddAttendanceWindow(QMainWindow):

    def __init__(self, parent=None):
        super(AddAttendanceWindow, self).__init__()
        self.ui = Ui_AddAttendanceWindow()
        self.ui.setupUi(self)
        
        self.parent = parent
        
        self.populateOrgBox()
        self.ui.uploadButton.clicked.connect(self.upload_attendance)
        
        today = date.today().strftime("%Y-%m-%d") + " (Today)"
        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d") + " (Yesterday)"
        self.ui.dateField.addItems([today, yesterday])
        self.ui.tableView.setStyleSheet(tableViewStyles)
            
        self.ui.confirmButton.hide()
        self.ui.confirmButton.clicked.connect(self.confirm_attendance)
    
            
    def populateOrgBox(self):
        stmt = "SELECT org_id, org_name FROM Organizations"
        cursor.execute(stmt)
        orgs = cursor.fetchall()
        
        for _id, name in orgs:
            self.ui.orgField.addItem(name, _id)
            
        self.ui.orgField.setCurrentIndex(0)
        
        
    @Slot()
    def confirm_attendance(self):
        org_id = self.ui.orgField.currentData()
        att_date = self.ui.dateField.currentText().split(" ")[0]
        
        # Check if attendance already exists
        stmt = f"SELECT atd_id FROM Attendance WHERE atd_date = '{att_date}' AND org_id = {org_id}"
        cursor.execute(stmt)
        if cursor.fetchone():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Attendance for this date already exists")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
          
        stmt = f"INSERT INTO Attendance (atd_date, org_id) VALUES ('{att_date}', {org_id})"
        print(stmt)
        cursor.execute(stmt)
        cursor.commit()
        
        stmt = f"SELECT atd_id FROM Attendance WHERE atd_date = '{att_date}' AND org_id = {org_id}"
        cursor.execute(stmt)
        atd_id = cursor.fetchone()[0]
        
        for ix in range(self.model.rowCount()):
            emp_id = self.model.data(self.model.index(ix, 0), Qt.DisplayRole)
            time_in = self.model.data(self.model.index(ix, 2), Qt.DisplayRole)
            time_out = self.model.data(self.model.index(ix, 3), Qt.DisplayRole)
            
            stmt = f"INSERT INTO AttendanceDetails (atd_id, emp_id, time_in, time_out) VALUES ({atd_id}, {emp_id}, '{time_in}', '{time_out}')"
            cursor.execute(stmt)
            cursor.commit()
            
        self.close()
        self.parent.loadData()
        
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
            
            self.ui.confirmButton.show()
        