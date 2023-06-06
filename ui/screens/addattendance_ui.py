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
        self.centralwidget = QWidget(AddAttendanceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.titleLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleLayout.addItem(self.horizontalSpacer)

        self.confirmButton = QPushButton(self.centralwidget)
        self.confirmButton.setObjectName(u"confirmButton")

        self.titleLayout.addWidget(self.confirmButton)

        self.dateField = QComboBox(self.centralwidget)
        self.dateField.setObjectName(u"dateField")

        self.titleLayout.addWidget(self.dateField)

        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.titleLayout.addWidget(self.uploadButton)


        self.mainLayout.addLayout(self.titleLayout)

        self.tableLayout = QHBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)


        self.mainLayout.addLayout(self.tableLayout)

        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 7)

        self.horizontalLayout.addLayout(self.mainLayout)

        AddAttendanceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddAttendanceWindow)

        QMetaObject.connectSlotsByName(AddAttendanceWindow)
    # setupUi

    def retranslateUi(self, AddAttendanceWindow):
        AddAttendanceWindow.setWindowTitle(QCoreApplication.translate("AddAttendanceWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddAttendanceWindow", u"Add New Attendance", None))
        self.confirmButton.setText(QCoreApplication.translate("AddAttendanceWindow", u"Confirm", None))
        self.uploadButton.setText(QCoreApplication.translate("AddAttendanceWindow", u"Upload Attendance", None))
    # retranslateUi

