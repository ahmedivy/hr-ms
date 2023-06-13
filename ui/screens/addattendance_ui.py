# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addattendance.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_AddAttendanceWindow(object):
    def setupUi(self, AddAttendanceWindow):
        if not AddAttendanceWindow.objectName():
            AddAttendanceWindow.setObjectName(u"AddAttendanceWindow")
        AddAttendanceWindow.resize(829, 672)
        AddAttendanceWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(AddAttendanceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 30px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.confirmButton = QPushButton(self.centralwidget)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color:white;\n"
"font:bold;\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"")

        self.horizontalLayout_2.addWidget(self.confirmButton)

        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color:white;\n"
"font:bold;\n"
"padding: 6px;\n"
"border-radius:8px;\n"
"")

        self.horizontalLayout_2.addWidget(self.uploadButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 16px;\n"
"color: white")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.dateField = QComboBox(self.centralwidget)
        self.dateField.setObjectName(u"dateField")
        self.dateField.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.dateField)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:16px;\n"
"color: white")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.orgField)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.mainLayout.addLayout(self.verticalLayout)

        self.tableLayout = QHBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)


        self.mainLayout.addLayout(self.tableLayout)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 7)

        self.horizontalLayout.addLayout(self.mainLayout)

        AddAttendanceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddAttendanceWindow)

        QMetaObject.connectSlotsByName(AddAttendanceWindow)
    # setupUi

    def retranslateUi(self, AddAttendanceWindow):
        AddAttendanceWindow.setWindowTitle(QCoreApplication.translate("AddAttendanceWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddAttendanceWindow", u"Add Attendance", None))
        self.confirmButton.setText(QCoreApplication.translate("AddAttendanceWindow", u"Confirm", None))
        self.uploadButton.setText(QCoreApplication.translate("AddAttendanceWindow", u"Upload Attendance", None))
        self.label_3.setText(QCoreApplication.translate("AddAttendanceWindow", u"Select Date", None))
        self.label_2.setText(QCoreApplication.translate("AddAttendanceWindow", u"Select Organization: ", None))
    # retranslateUi

