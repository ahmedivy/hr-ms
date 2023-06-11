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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AddEmployeeWindow(object):
    def setupUi(self, AddEmployeeWindow):
        if not AddEmployeeWindow.objectName():
            AddEmployeeWindow.setObjectName(u"AddEmployeeWindow")
        AddEmployeeWindow.resize(792, 746)
        AddEmployeeWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(AddEmployeeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"border-radius:15px;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"max-width:400px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;\n"
"text-align:centre;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.fnameField = QLineEdit(self.frame_2)
        self.fnameField.setObjectName(u"fnameField")
        self.fnameField.setMaximumSize(QSize(250, 16777215))
        self.fnameField.setStyleSheet(u"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;\n"
"margin: 3px 0;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fnameField)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;\n"
"text-align:centre;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lnameField = QLineEdit(self.frame_2)
        self.lnameField.setObjectName(u"lnameField")
        self.lnameField.setStyleSheet(u"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;\n"
"margin: 3px 0;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lnameField)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.cnicField = QLineEdit(self.frame_2)
        self.cnicField.setObjectName(u"cnicField")
        self.cnicField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cnicField)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.phoneField = QLineEdit(self.frame_2)
        self.phoneField.setObjectName(u"phoneField")
        self.phoneField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.phoneField)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.emailField = QLineEdit(self.frame_2)
        self.emailField.setObjectName(u"emailField")
        self.emailField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"margin: 3px 0;")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.emailField)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"margin: 3px 0;border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"margin: 3px 0;border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.dateEdit)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.addressField = QLineEdit(self.frame_2)
        self.addressField.setObjectName(u"addressField")
        self.addressField.setStyleSheet(u"margin: 3px 0;border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.addressField)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_10)

        self.cityField = QLineEdit(self.frame_2)
        self.cityField.setObjectName(u"cityField")
        self.cityField.setStyleSheet(u"margin: 3px 0;border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.cityField)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_11)

        self.stateField = QLineEdit(self.frame_2)
        self.stateField.setObjectName(u"stateField")
        self.stateField.setStyleSheet(u"margin: 3px 0;background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.stateField)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_12)

        self.countryField = QLineEdit(self.frame_2)
        self.countryField.setObjectName(u"countryField")
        self.countryField.setStyleSheet(u"margin: 3px 0;background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.countryField)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_13)

        self.zipField = QLineEdit(self.frame_2)
        self.zipField.setObjectName(u"zipField")
        self.zipField.setStyleSheet(u"margin: 3px 0;background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"max-width:250px;\n"
"height: 25px;")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.zipField)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(self.frame_3)
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

        self.okButton = QPushButton(self.frame_3)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.okButton)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        AddEmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEmployeeWindow)

        QMetaObject.connectSlotsByName(AddEmployeeWindow)
    # setupUi

    def retranslateUi(self, AddEmployeeWindow):
        AddEmployeeWindow.setWindowTitle(QCoreApplication.translate("AddEmployeeWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddEmployeeWindow", u"ADD NEW EMPLOYEE", None))
        self.label_2.setText(QCoreApplication.translate("AddEmployeeWindow", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("AddEmployeeWindow", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("AddEmployeeWindow", u"CNIC", None))
        self.label_5.setText(QCoreApplication.translate("AddEmployeeWindow", u"Phone Number", None))
        self.label_6.setText(QCoreApplication.translate("AddEmployeeWindow", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("AddEmployeeWindow", u"Position", None))
        self.label_8.setText(QCoreApplication.translate("AddEmployeeWindow", u"Date of Birth", None))
        self.label_9.setText(QCoreApplication.translate("AddEmployeeWindow", u"Address", None))
        self.label_10.setText(QCoreApplication.translate("AddEmployeeWindow", u"City", None))
        self.label_11.setText(QCoreApplication.translate("AddEmployeeWindow", u"State", None))
        self.label_12.setText(QCoreApplication.translate("AddEmployeeWindow", u"Country", None))
        self.label_13.setText(QCoreApplication.translate("AddEmployeeWindow", u"Zip code", None))
        self.cancelButton.setText(QCoreApplication.translate("AddEmployeeWindow", u"Cancel", None))
        self.okButton.setText(QCoreApplication.translate("AddEmployeeWindow", u"Confirm", None))
    # retranslateUi

