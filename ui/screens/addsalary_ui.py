# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addsalary.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddSalaryWindow(object):
    def setupUi(self, AddSalaryWindow):
        if not AddSalaryWindow.objectName():
            AddSalaryWindow.setObjectName(u"AddSalaryWindow")
        AddSalaryWindow.resize(586, 425)
        AddSalaryWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(AddSalaryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"border-radius:15px;\n"
"padding: 0 auto;\n"
"margin: 0 20px;\n"
"max-height:80px;\n"
"max-width:420px;\n"
"text-transform:uppercase;\n"
"\n"
"\n"
"\n"
"")

        self.titleLayout.addWidget(self.label)


        self.mainLayout.addLayout(self.titleLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 30, 20, 20)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;\n"
"margin: 0 20px;")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;\n"
"")

        self.gridLayout.addWidget(self.orgField, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;\n"
"margin: 0 20px;")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.monthField = QComboBox(self.centralwidget)
        self.monthField.setObjectName(u"monthField")
        self.monthField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.gridLayout.addWidget(self.monthField, 1, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;\n"
"margin: 0 20px;")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.yearField = QComboBox(self.centralwidget)
        self.yearField.setObjectName(u"yearField")
        self.yearField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.gridLayout.addWidget(self.yearField, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;\n"
"margin: 0 20px;")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.descField = QLineEdit(self.centralwidget)
        self.descField.setObjectName(u"descField")
        self.descField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.gridLayout.addWidget(self.descField, 3, 1, 1, 1)


        self.mainLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.confirmButton = QPushButton(self.centralwidget)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setStyleSheet(u"QPushButton{\n"
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
"")

        self.horizontalLayout_2.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setStyleSheet(u"QPushButton{\n"
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
"")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.horizontalLayout_2)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 8)
        self.mainLayout.setStretch(2, 2)

        self.horizontalLayout.addLayout(self.mainLayout)

        AddSalaryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddSalaryWindow)

        QMetaObject.connectSlotsByName(AddSalaryWindow)
    # setupUi

    def retranslateUi(self, AddSalaryWindow):
        AddSalaryWindow.setWindowTitle(QCoreApplication.translate("AddSalaryWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddSalaryWindow", u"Generate Salary Slip", None))
        self.label_2.setText(QCoreApplication.translate("AddSalaryWindow", u"Organization", None))
        self.label_3.setText(QCoreApplication.translate("AddSalaryWindow", u"Salary Month", None))
        self.label_4.setText(QCoreApplication.translate("AddSalaryWindow", u"Salary Year", None))
        self.label_5.setText(QCoreApplication.translate("AddSalaryWindow", u"Description", None))
        self.confirmButton.setText(QCoreApplication.translate("AddSalaryWindow", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddSalaryWindow", u"Cancel", None))
    # retranslateUi

