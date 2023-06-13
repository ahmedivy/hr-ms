from datetime import date
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import cursor
from views.addloan import AddLoanWindow
from ui.static.css import tableViewStyles
from ui.widgets.loanwidget_ui import Ui_LoanWidget


class LoanTableModel(QAbstractTableModel):
    
    def __init__(self, loans: list):
        super(LoanTableModel, self).__init__()
        self.loans = loans
        self.header = [
            "Employee ID",
            "Employee Name",
            "Organization",
            "Amount",
            "Date",
            "Status",
            "Payment Date",
            "Actions"
        ]
        
    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.loans)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            loan = self.loans[index.row()]
            if index.column() == 0:
                return loan[0]
            elif index.column() == 1:
                return loan[1]
            elif index.column() == 2:
                return loan[3]
            elif index.column() == 3:
                return str(loan[5])
            elif index.column() == 4:
                return str(loan[6])
            elif index.column() == 5:
                return str(loan[7])
            elif index.column() == 6:
                return str(loan[8])         
            
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]


class LoanWidget(QWidget):
    def __init__(self):
        super(LoanWidget, self).__init__()
        self.ui = Ui_LoanWidget()
        self.ui.setupUi(self)
        
        # Populate the table
        self.populateComboBox()
        self.loadData()
        self.ui.tableView.setStyleSheet(tableViewStyles)
        
        self.addButtons()
        self.ui.addButton.clicked.connect(self.handleNew)
        self.ui.pendingCheckbox.hide()
        
    def loadData(self):
        stmt = f'EXEC GetLoans {self.ui.orgField.currentData()}'
        cursor.execute(stmt)
        loans = cursor.fetchall()
        self.model = LoanTableModel(loans)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addButtons()
        
    
    def populateComboBox(self):
        stmt = 'SELECT o.org_id, o.org_name FROM Organizations o'
        cursor.execute(stmt)
        orgs = cursor.fetchall()
        
        for _id, name in orgs:
            self.ui.orgField.addItem(name, _id)
            
        self.ui.orgField.setCurrentIndex(0)
        self.ui.orgField.currentIndexChanged.connect(self.handleOrgChange)
        
    @Slot()
    def handleOrgChange(self):
        self.loadData()
        
    @Slot()
    def handleNew(self):
        self.addLoanWindow = AddLoanWindow()
        self.addLoanWindow.show()
        
        
    def addButtons(self):
        for ix in range(self.model.rowCount()):
            index_value = self.model.index(ix, 5).data()
            
            if index_value != "Paid":
                button = QPushButton("Payment Done", self)
                button.clicked.connect(self.handleClick)
                self.ui.tableView.setIndexWidget(self.ui.tableView.model().index(ix, 7), button)

            
    @Slot()
    def handleClick(self):
        button = self.sender()
        index = self.ui.tableView.indexAt(button.pos())
        loan = self.model.loans[index.row()]
        
        stmt = f"UPDATE Loans SET loan_status = 'Paid', loan_payment_date = {date.today()} WHERE loan_id = {loan[4]}"
        cursor.execute(stmt)
        cursor.commit()
        
        self.loadData()
        
    