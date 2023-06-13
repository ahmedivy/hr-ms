# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_EmployeeWidget(object):
    def setupUi(self, EmployeeWidget):
        if not EmployeeWidget.objectName():
            EmployeeWidget.setObjectName(u"EmployeeWidget")
        EmployeeWidget.resize(1054, 844)
        self.horizontalLayout_2 = QHBoxLayout(EmployeeWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleBar = QHBoxLayout()
        self.titleBar.setObjectName(u"titleBar")
        self.searchField = QLineEdit(EmployeeWidget)
        self.searchField.setObjectName(u"searchField")
        self.searchField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"width:250px;\n"
"height: 25px;\n"
"margin: 3px 0;")

        self.titleBar.addWidget(self.searchField)

        self.searchButton = QPushButton(EmployeeWidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4cc9f0;\n"
"  color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
" background-color: rgb(255, 233, 67);\n"
"  color:black;\n"
"font:bold;\n"
"padding: 3px;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.titleBar.addWidget(self.searchButton)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleBar.addItem(self.spacer)

        self.addButton = QPushButton(EmployeeWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4cc9f0;\n"
"  color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
" background-color: rgb(255, 233, 67);\n"
"  color:black;\n"
"font:bold;\n"
"padding: 3px;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.titleBar.addWidget(self.addButton)


        self.mainLayout.addLayout(self.titleBar)

        self.tableLayout = QVBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.filterBar = QHBoxLayout()
        self.filterBar.setObjectName(u"filterBar")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filterBar.addItem(self.horizontalSpacer)

        self.orgField = QComboBox(EmployeeWidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"font-size: 18px;\n"
"color: black;\n"
"background-color: white")

        self.filterBar.addWidget(self.orgField)


        self.tableLayout.addLayout(self.filterBar)

        self.tableView = QTableView(EmployeeWidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)

        self.tableLayout.setStretch(0, 1)
        self.tableLayout.setStretch(1, 8)

        self.mainLayout.addLayout(self.tableLayout)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout_2.addLayout(self.mainLayout)


        self.retranslateUi(EmployeeWidget)

        QMetaObject.connectSlotsByName(EmployeeWidget)
    # setupUi

    def retranslateUi(self, EmployeeWidget):
        EmployeeWidget.setWindowTitle(QCoreApplication.translate("EmployeeWidget", u"Form", None))
        self.searchButton.setText(QCoreApplication.translate("EmployeeWidget", u"Search", None))
        self.addButton.setText(QCoreApplication.translate("EmployeeWidget", u"Add Employee", None))
    # retranslateUi

