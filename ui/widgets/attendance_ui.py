# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendance.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_AttendanceWidget(object):
    def setupUi(self, AttendanceWidget):
        if not AttendanceWidget.objectName():
            AttendanceWidget.setObjectName(u"AttendanceWidget")
        AttendanceWidget.resize(1009, 741)
        self.horizontalLayout = QHBoxLayout(AttendanceWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.label = QLabel(AttendanceWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 35px\n"
"")

        self.titleLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleLayout.addItem(self.horizontalSpacer)

        self.addButton = QPushButton(AttendanceWidget)
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

        self.titleLayout.addWidget(self.addButton)


        self.mainLayout.addLayout(self.titleLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterBar = QHBoxLayout()
        self.filterBar.setObjectName(u"filterBar")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filterBar.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(AttendanceWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;\n"
"font-size: 20px")

        self.filterBar.addWidget(self.label_2)

        self.orgField = QComboBox(AttendanceWidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"background-color:#FFFAFB;\n"
"width:250px;\n"
"height: 25px;\n"
"margin: 3px 0;")

        self.filterBar.addWidget(self.orgField)


        self.verticalLayout.addLayout(self.filterBar)

        self.tableView = QTableView(AttendanceWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)

        self.mainLayout.addLayout(self.verticalLayout)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 12)

        self.horizontalLayout.addLayout(self.mainLayout)


        self.retranslateUi(AttendanceWidget)

        QMetaObject.connectSlotsByName(AttendanceWidget)
    # setupUi

    def retranslateUi(self, AttendanceWidget):
        AttendanceWidget.setWindowTitle(QCoreApplication.translate("AttendanceWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AttendanceWidget", u"Attendance", None))
        self.addButton.setText(QCoreApplication.translate("AttendanceWidget", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("AttendanceWidget", u"Select Organization: ", None))
    # retranslateUi

