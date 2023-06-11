from sqlmodel import text
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

from core.database import engine, cursor
from views.addloan import AddLoanWindow
from ui.widgets.loanwidget_ui import Ui_LoanWidget


class LoanTableModel(QAbstractTableModel):
    
    def __init__(self, loans: list):
        super(LoanTableModel, self).__init__()
        self.loans = loans
        self.filtered_loans = loans
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
        return len(self.filtered_loans)
    
    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.header)
    
    def data(self, index: QModelIndex, role: int = None):
        if role == Qt.DisplayRole:
            loan = self.filtered_loans[index.row()]
            if index.column() == 0:
                return loan[0]
            elif index.column() == 1:
                return loan[1]
            elif index.column() == 2:
                return loan[3]
            elif index.column() == 3:
                return loan[5]
            elif index.column() == 4:
                return loan[6]
            elif index.column() == 5:
                return loan[7]
            elif index.column() == 6:
                return loan[8]         
            
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
        self.loadData()
        
        self.addButtons()
        self.populateComboBox()
        self.ui.addButton.clicked.connect(self.handleNew)
        # self.ui.pendingCheckbox.
        
    def loadData(self):
        with engine.connect() as conn:
            stmt = text("EXEC GetLoans")
            result = conn.execute(stmt)
            loans = result.fetchall()
            print(loans)
            
        self.model = LoanTableModel(loans)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addButtons()
        
    
    def populateComboBox(self):
        with engine.connect() as conn:
            stmt = text(
                "SELECT o.org_id, o.org_name FROM Organizations o"
            )
            result = conn.execute(stmt)
            organizations = result.fetchall()
            
        self.ui.orgField.clear()
        self.ui.orgField.addItem("All Organization", -1)
        
        for org in organizations:
            self.ui.orgField.addItem(org.org_name, org.org_id)
            
        # Add Default Item
        self.ui.orgField.setCurrentIndex(0)
        
        # Connect the signal
        self.ui.orgField.currentIndexChanged.connect(self.handleOrgChange)
        
    @Slot()
    def handleOrgChange(self):
        # Update the filtered loans
        org_id = self.ui.orgField.currentData()
        
        if org_id == -1:
            self.model.filtered_loans = self.model.loans
        else:
            self.model.filtered_loans = [
                loan for loan in self.model.loans if loan.org_id == org_id
            ]
            
        self.model.layoutChanged.emit()
        
    @Slot()
    def handleNew(self):
        self.addLoanWindow = AddLoanWindow()
        self.addLoanWindow.show()
        
        
    def addButtons(self):
        for ix in range(self.model.rowCount()):
            button = QPushButton("Payment Done", self)
            button.clicked.connect(self.handleClick)
            self.ui.tableView.setIndexWidget(self.ui.tableView.model().index(ix, 7), button)
            
    @Slot()
    def handleClick(self):
        button = self.sender()
        index = self.ui.tableView.indexAt(button.pos())
        loan = self.model.filtered_loans[index.row()]
        
        with engine.connect() as conn:
            stmt = text(
            f"EXEC UpdateLoanStatus {loan[4]}"
            )
            conn.execute(stmt)
            
        self.loadData()
        
    