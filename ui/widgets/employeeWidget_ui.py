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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
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

        self.titleBar.addWidget(self.searchField)

        self.searchButton = QPushButton(EmployeeWidget)
        self.searchButton.setObjectName(u"searchButton")

        self.titleBar.addWidget(self.searchButton)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleBar.addItem(self.spacer)

        self.pushButton_2 = QPushButton(EmployeeWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.titleBar.addWidget(self.pushButton_2)


        self.mainLayout.addLayout(self.titleBar)

        self.tableFrame = QFrame(EmployeeWidget)
        self.tableFrame.setObjectName(u"tableFrame")
        self.tableFrame.setFrameShape(QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.tableFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.tableView = QTableView(self.tableFrame)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)


        self.mainLayout.addWidget(self.tableFrame)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout_2.addLayout(self.mainLayout)


        self.retranslateUi(EmployeeWidget)

        QMetaObject.connectSlotsByName(EmployeeWidget)
    # setupUi

    def retranslateUi(self, EmployeeWidget):
        EmployeeWidget.setWindowTitle(QCoreApplication.translate("EmployeeWidget", u"Form", None))
        self.searchButton.setText(QCoreApplication.translate("EmployeeWidget", u"Search", None))
        self.pushButton_2.setText(QCoreApplication.translate("EmployeeWidget", u"PushButton", None))
    # retranslateUi

