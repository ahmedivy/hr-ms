# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loanwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_LoanWidget(object):
    def setupUi(self, LoanWidget):
        if not LoanWidget.objectName():
            LoanWidget.setObjectName(u"LoanWidget")
        LoanWidget.resize(821, 647)
        self.horizontalLayout = QHBoxLayout(LoanWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleBar = QHBoxLayout()
        self.titleBar.setObjectName(u"titleBar")
        self.label = QLabel(LoanWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 30px;\n"
"color: white;")

        self.titleBar.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleBar.addItem(self.horizontalSpacer_3)

        self.addButton = QPushButton(LoanWidget)
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


        self.titleLayout.addLayout(self.titleBar)

        self.filterBar = QHBoxLayout()
        self.filterBar.setObjectName(u"filterBar")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filterBar.addItem(self.horizontalSpacer)

        self.pendingCheckbox = QCheckBox(LoanWidget)
        self.pendingCheckbox.setObjectName(u"pendingCheckbox")
        self.pendingCheckbox.setStyleSheet(u"color:white\n"
"")

        self.filterBar.addWidget(self.pendingCheckbox)

        self.orgField = QComboBox(LoanWidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"color: white;\n"
"font-size: 16px\n"
"")

        self.filterBar.addWidget(self.orgField)


        self.titleLayout.addLayout(self.filterBar)


        self.mainLayout.addLayout(self.titleLayout)

        self.tableLayout = QHBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.tableView = QTableView(LoanWidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)


        self.mainLayout.addLayout(self.tableLayout)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout.addLayout(self.mainLayout)


        self.retranslateUi(LoanWidget)

        QMetaObject.connectSlotsByName(LoanWidget)
    # setupUi

    def retranslateUi(self, LoanWidget):
        LoanWidget.setWindowTitle(QCoreApplication.translate("LoanWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoanWidget", u"Loans Information", None))
        self.addButton.setText(QCoreApplication.translate("LoanWidget", u"Add", None))
        self.pendingCheckbox.setText(QCoreApplication.translate("LoanWidget", u"Pending", None))
    # retranslateUi

