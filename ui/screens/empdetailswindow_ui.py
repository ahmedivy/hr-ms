# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'empdetailswindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_EmployeeDetailsWindow(object):
    def setupUi(self, EmployeeDetailsWindow):
        if not EmployeeDetailsWindow.objectName():
            EmployeeDetailsWindow.setObjectName(u"EmployeeDetailsWindow")
        EmployeeDetailsWindow.resize(508, 732)
        EmployeeDetailsWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(EmployeeDetailsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleBar = QHBoxLayout()
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setContentsMargins(20, 10, 20, 10)
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 0 5px;\n"
"border-radius:10px;\n"
"")

        self.titleBar.addWidget(self.nameLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titleBar.addItem(self.horizontalSpacer)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"height:25px;\n"
"margin-right:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: #4cc9f0;\n"
" color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}")

        self.titleBar.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"height:25px;\n"
"margin-right:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: #4cc9f0;\n"
" color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}")

        self.titleBar.addWidget(self.deleteButton)


        self.mainLayout.addLayout(self.titleBar)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(20, 10, 20, 10)
        self.codeLabel = QLabel(self.centralwidget)
        self.codeLabel.setObjectName(u"codeLabel")
        self.codeLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.codeLabel)

        self.codeField = QLineEdit(self.centralwidget)
        self.codeField.setObjectName(u"codeField")
        self.codeField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.codeField)

        self.fnameLabel = QLabel(self.centralwidget)
        self.fnameLabel.setObjectName(u"fnameLabel")
        self.fnameLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.fnameLabel)

        self.fnameField = QLineEdit(self.centralwidget)
        self.fnameField.setObjectName(u"fnameField")
        self.fnameField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.fnameField)

        self.lnameLabel = QLabel(self.centralwidget)
        self.lnameLabel.setObjectName(u"lnameLabel")
        self.lnameLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lnameLabel)

        self.lnameField = QLineEdit(self.centralwidget)
        self.lnameField.setObjectName(u"lnameField")
        self.lnameField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lnameField)

        self.orgLabel = QLabel(self.centralwidget)
        self.orgLabel.setObjectName(u"orgLabel")
        self.orgLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.orgLabel)

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.orgField)

        self.posLabel = QLabel(self.centralwidget)
        self.posLabel.setObjectName(u"posLabel")
        self.posLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.posLabel)

        self.posField = QLineEdit(self.centralwidget)
        self.posField.setObjectName(u"posField")
        self.posField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.posField)

        self.cnicLabel = QLabel(self.centralwidget)
        self.cnicLabel.setObjectName(u"cnicLabel")
        self.cnicLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.cnicLabel)

        self.cnicField = QLineEdit(self.centralwidget)
        self.cnicField.setObjectName(u"cnicField")
        self.cnicField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cnicField)

        self.hireDateLabel = QLabel(self.centralwidget)
        self.hireDateLabel.setObjectName(u"hireDateLabel")
        self.hireDateLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.hireDateLabel)

        self.hireDateField = QDateEdit(self.centralwidget)
        self.hireDateField.setObjectName(u"hireDateField")
        self.hireDateField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.hireDateField)

        self.terminationDateLabel = QLabel(self.centralwidget)
        self.terminationDateLabel.setObjectName(u"terminationDateLabel")
        self.terminationDateLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.terminationDateLabel)

        self.terminationDateField = QLineEdit(self.centralwidget)
        self.terminationDateField.setObjectName(u"terminationDateField")
        self.terminationDateField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.terminationDateField)

        self.rateLabel = QLabel(self.centralwidget)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.rateLabel)

        self.rateField = QDoubleSpinBox(self.centralwidget)
        self.rateField.setObjectName(u"rateField")
        self.rateField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.rateField)

        self.emailLabel = QLabel(self.centralwidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.emailLabel)

        self.emailField = QLineEdit(self.centralwidget)
        self.emailField.setObjectName(u"emailField")
        self.emailField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.emailField)

        self.numberLabel = QLabel(self.centralwidget)
        self.numberLabel.setObjectName(u"numberLabel")
        self.numberLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.numberLabel)

        self.phoneField = QLineEdit(self.centralwidget)
        self.phoneField.setObjectName(u"phoneField")
        self.phoneField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.phoneField)

        self.streetLabel = QLabel(self.centralwidget)
        self.streetLabel.setObjectName(u"streetLabel")
        self.streetLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.streetLabel)

        self.streetField = QLineEdit(self.centralwidget)
        self.streetField.setObjectName(u"streetField")
        self.streetField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.streetField)

        self.cityLabel = QLabel(self.centralwidget)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.cityLabel)

        self.cityField = QLineEdit(self.centralwidget)
        self.cityField.setObjectName(u"cityField")
        self.cityField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.cityField)

        self.stateLabel = QLabel(self.centralwidget)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.stateLabel)

        self.stateField = QLineEdit(self.centralwidget)
        self.stateField.setObjectName(u"stateField")
        self.stateField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.stateField)

        self.zipLabel = QLabel(self.centralwidget)
        self.zipLabel.setObjectName(u"zipLabel")
        self.zipLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.zipLabel)

        self.zipField = QLineEdit(self.centralwidget)
        self.zipField.setObjectName(u"zipField")
        self.zipField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.zipField)

        self.countryLabel = QLabel(self.centralwidget)
        self.countryLabel.setObjectName(u"countryLabel")
        self.countryLabel.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.countryLabel)

        self.countryField = QLineEdit(self.centralwidget)
        self.countryField.setObjectName(u"countryField")
        self.countryField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.countryField)


        self.mainLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout.addLayout(self.mainLayout)

        EmployeeDetailsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeDetailsWindow)

        QMetaObject.connectSlotsByName(EmployeeDetailsWindow)
    # setupUi

    def retranslateUi(self, EmployeeDetailsWindow):
        EmployeeDetailsWindow.setWindowTitle(QCoreApplication.translate("EmployeeDetailsWindow", u"MainWindow", None))
        self.nameLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Ahmed Abdullah", None))
        self.editButton.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Delete", None))
        self.codeLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Employee Code", None))
        self.fnameLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"First Name", None))
        self.lnameLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Last Name", None))
        self.orgLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Organization", None))
        self.posLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Position", None))
        self.cnicLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"CNIC", None))
        self.hireDateLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Hire Date", None))
        self.terminationDateLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Termination Date", None))
        self.rateLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Hourly Rate", None))
        self.emailLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Email", None))
        self.numberLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Phone Number", None))
        self.streetLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Street Address", None))
        self.cityLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"City", None))
        self.stateLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"State", None))
        self.zipLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Zip Code", None))
        self.countryLabel.setText(QCoreApplication.translate("EmployeeDetailsWindow", u"Country", None))
    # retranslateUi

