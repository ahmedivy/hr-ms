# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addemployee.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AddEmployeeWindow(object):
    def setupUi(self, AddEmployeeWindow):
        if not AddEmployeeWindow.objectName():
            AddEmployeeWindow.setObjectName(u"AddEmployeeWindow")
        AddEmployeeWindow.resize(508, 732)
        AddEmployeeWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(AddEmployeeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleBar = QHBoxLayout()
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setContentsMargins(20, 10, 20, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 35px;\n"
"color: white")

        self.titleBar.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleBar.addItem(self.horizontalSpacer)


        self.mainLayout.addLayout(self.titleBar)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(20, 10, 20, 10)
        self.fnameLabel = QLabel(self.centralwidget)
        self.fnameLabel.setObjectName(u"fnameLabel")
        self.fnameLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fnameLabel)

        self.fnameField = QLineEdit(self.centralwidget)
        self.fnameField.setObjectName(u"fnameField")
        self.fnameField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fnameField)

        self.lnameLabel = QLabel(self.centralwidget)
        self.lnameLabel.setObjectName(u"lnameLabel")
        self.lnameLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lnameLabel)

        self.lnameField = QLineEdit(self.centralwidget)
        self.lnameField.setObjectName(u"lnameField")
        self.lnameField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lnameField)

        self.orgLabel = QLabel(self.centralwidget)
        self.orgLabel.setObjectName(u"orgLabel")
        self.orgLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.orgLabel)

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.orgField)

        self.posLabel = QLabel(self.centralwidget)
        self.posLabel.setObjectName(u"posLabel")
        self.posLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.posLabel)

        self.posField = QLineEdit(self.centralwidget)
        self.posField.setObjectName(u"posField")
        self.posField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.posField)

        self.cnicLabel = QLabel(self.centralwidget)
        self.cnicLabel.setObjectName(u"cnicLabel")
        self.cnicLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cnicLabel)

        self.cnicField = QLineEdit(self.centralwidget)
        self.cnicField.setObjectName(u"cnicField")
        self.cnicField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cnicField)

        self.rateLabel = QLabel(self.centralwidget)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.rateLabel)

        self.rateField = QDoubleSpinBox(self.centralwidget)
        self.rateField.setObjectName(u"rateField")
        self.rateField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.rateField)

        self.emailLabel = QLabel(self.centralwidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.emailLabel)

        self.emailField = QLineEdit(self.centralwidget)
        self.emailField.setObjectName(u"emailField")
        self.emailField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.emailField)

        self.numberLabel = QLabel(self.centralwidget)
        self.numberLabel.setObjectName(u"numberLabel")
        self.numberLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.numberLabel)

        self.phoneField = QLineEdit(self.centralwidget)
        self.phoneField.setObjectName(u"phoneField")
        self.phoneField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.phoneField)

        self.streetLabel = QLabel(self.centralwidget)
        self.streetLabel.setObjectName(u"streetLabel")
        self.streetLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.streetLabel)

        self.streetField = QLineEdit(self.centralwidget)
        self.streetField.setObjectName(u"streetField")
        self.streetField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.streetField)

        self.cityLabel = QLabel(self.centralwidget)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.cityLabel)

        self.cityField = QLineEdit(self.centralwidget)
        self.cityField.setObjectName(u"cityField")
        self.cityField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.cityField)

        self.stateLabel = QLabel(self.centralwidget)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.stateLabel)

        self.stateField = QLineEdit(self.centralwidget)
        self.stateField.setObjectName(u"stateField")
        self.stateField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.stateField)

        self.zipLabel = QLabel(self.centralwidget)
        self.zipLabel.setObjectName(u"zipLabel")
        self.zipLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.zipLabel)

        self.zipField = QLineEdit(self.centralwidget)
        self.zipField.setObjectName(u"zipField")
        self.zipField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.zipField)

        self.countryLabel = QLabel(self.centralwidget)
        self.countryLabel.setObjectName(u"countryLabel")
        self.countryLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.countryLabel)

        self.countryField = QLineEdit(self.centralwidget)
        self.countryField.setObjectName(u"countryField")
        self.countryField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.countryField)


        self.mainLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

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
"\n"
"QPushButton:clicked{\n"
" background-color: rgb(255, 233, 67);\n"
"  color:black;\n"
"font:bold;\n"
"padding: 3px;\n"
"border-radius:10px;\n"
"\n"
"}")

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
"\n"
"QPushButton:clicked{\n"
" background-color: rgb(255, 233, 67);\n"
"  color:black;\n"
"font:bold;\n"
"padding: 3px;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.horizontalLayout_2)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout.addLayout(self.mainLayout)

        AddEmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEmployeeWindow)

        QMetaObject.connectSlotsByName(AddEmployeeWindow)
    # setupUi

    def retranslateUi(self, AddEmployeeWindow):
        AddEmployeeWindow.setWindowTitle(QCoreApplication.translate("AddEmployeeWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddEmployeeWindow", u"Add Employee", None))
        self.fnameLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"First Name", None))
        self.lnameLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Last Name", None))
        self.orgLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Organization", None))
        self.posLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Position", None))
        self.cnicLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"CNIC", None))
        self.rateLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Hourly Rate", None))
        self.emailLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Email", None))
        self.numberLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Phone Number", None))
        self.streetLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Street Address", None))
        self.cityLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"City", None))
        self.stateLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"State", None))
        self.zipLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Zip Code", None))
        self.countryLabel.setText(QCoreApplication.translate("AddEmployeeWindow", u"Country", None))
        self.confirmButton.setText(QCoreApplication.translate("AddEmployeeWindow", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddEmployeeWindow", u"Cancel", None))
    # retranslateUi

