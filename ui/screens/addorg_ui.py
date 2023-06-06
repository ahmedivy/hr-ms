# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addorg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AddOrgWindow(object):
    def setupUi(self, AddOrgWindow):
        if not AddOrgWindow.objectName():
            AddOrgWindow.setObjectName(u"AddOrgWindow")
        AddOrgWindow.resize(951, 585)
        self.centralwidget = QWidget(AddOrgWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setContentsMargins(20, 20, 20, 20)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(26)
        self.titleLabel.setFont(font)

        self.titleLayout.addWidget(self.titleLabel)


        self.mainLayout.addLayout(self.titleLayout)

        self.mainFormLayout = QHBoxLayout()
        self.mainFormLayout.setObjectName(u"mainFormLayout")
        self.mainBox = QGroupBox(self.centralwidget)
        self.mainBox.setObjectName(u"mainBox")
        font1 = QFont()
        font1.setPointSize(12)
        self.mainBox.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.mainBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainForm = QFormLayout()
        self.mainForm.setObjectName(u"mainForm")
        self.mainForm.setHorizontalSpacing(20)
        self.mainForm.setVerticalSpacing(20)
        self.mainForm.setContentsMargins(20, 20, 20, 20)
        self.label_2 = QLabel(self.mainBox)
        self.label_2.setObjectName(u"label_2")

        self.mainForm.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.mainBox)
        self.label_3.setObjectName(u"label_3")

        self.mainForm.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.mainBox)
        self.label_4.setObjectName(u"label_4")

        self.mainForm.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.mainBox)
        self.label_5.setObjectName(u"label_5")

        self.mainForm.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.mainBox)
        self.label_6.setObjectName(u"label_6")

        self.mainForm.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.nameField = QLineEdit(self.mainBox)
        self.nameField.setObjectName(u"nameField")

        self.mainForm.setWidget(0, QFormLayout.FieldRole, self.nameField)

        self.phoneField = QLineEdit(self.mainBox)
        self.phoneField.setObjectName(u"phoneField")

        self.mainForm.setWidget(2, QFormLayout.FieldRole, self.phoneField)

        self.emailField = QLineEdit(self.mainBox)
        self.emailField.setObjectName(u"emailField")

        self.mainForm.setWidget(3, QFormLayout.FieldRole, self.emailField)

        self.websiteField = QLineEdit(self.mainBox)
        self.websiteField.setObjectName(u"websiteField")

        self.mainForm.setWidget(4, QFormLayout.FieldRole, self.websiteField)

        self.typeField = QComboBox(self.mainBox)
        self.typeField.setObjectName(u"typeField")

        self.mainForm.setWidget(1, QFormLayout.FieldRole, self.typeField)


        self.horizontalLayout_2.addLayout(self.mainForm)


        self.mainFormLayout.addWidget(self.mainBox)

        self.addressBox = QGroupBox(self.centralwidget)
        self.addressBox.setObjectName(u"addressBox")
        self.addressBox.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.addressBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.addressForm = QFormLayout()
        self.addressForm.setObjectName(u"addressForm")
        self.addressForm.setHorizontalSpacing(20)
        self.addressForm.setVerticalSpacing(20)
        self.addressForm.setContentsMargins(20, 20, 20, 20)
        self.label_7 = QLabel(self.addressBox)
        self.label_7.setObjectName(u"label_7")

        self.addressForm.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.addressBox)
        self.label_8.setObjectName(u"label_8")

        self.addressForm.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.addressBox)
        self.label_9.setObjectName(u"label_9")

        self.addressForm.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.addressBox)
        self.label_10.setObjectName(u"label_10")

        self.addressForm.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.addressBox)
        self.label_11.setObjectName(u"label_11")

        self.addressForm.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.streetField = QLineEdit(self.addressBox)
        self.streetField.setObjectName(u"streetField")

        self.addressForm.setWidget(0, QFormLayout.FieldRole, self.streetField)

        self.cityField = QLineEdit(self.addressBox)
        self.cityField.setObjectName(u"cityField")

        self.addressForm.setWidget(1, QFormLayout.FieldRole, self.cityField)

        self.stateField = QLineEdit(self.addressBox)
        self.stateField.setObjectName(u"stateField")

        self.addressForm.setWidget(2, QFormLayout.FieldRole, self.stateField)

        self.countryField = QLineEdit(self.addressBox)
        self.countryField.setObjectName(u"countryField")

        self.addressForm.setWidget(3, QFormLayout.FieldRole, self.countryField)

        self.zipField = QLineEdit(self.addressBox)
        self.zipField.setObjectName(u"zipField")

        self.addressForm.setWidget(4, QFormLayout.FieldRole, self.zipField)


        self.horizontalLayout_3.addLayout(self.addressForm)


        self.mainFormLayout.addWidget(self.addressBox)


        self.mainLayout.addLayout(self.mainFormLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        font2 = QFont()
        font2.setPointSize(11)
        self.okButton.setFont(font2)

        self.buttonsLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setFont(font2)

        self.buttonsLayout.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.buttonsLayout)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 6)
        self.mainLayout.setStretch(3, 3)

        self.verticalLayout_2.addLayout(self.mainLayout)

        AddOrgWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.nameField, self.typeField)
        QWidget.setTabOrder(self.typeField, self.phoneField)
        QWidget.setTabOrder(self.phoneField, self.emailField)
        QWidget.setTabOrder(self.emailField, self.websiteField)
        QWidget.setTabOrder(self.websiteField, self.streetField)
        QWidget.setTabOrder(self.streetField, self.cityField)
        QWidget.setTabOrder(self.cityField, self.stateField)
        QWidget.setTabOrder(self.stateField, self.countryField)
        QWidget.setTabOrder(self.countryField, self.zipField)
        QWidget.setTabOrder(self.zipField, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(AddOrgWindow)

        QMetaObject.connectSlotsByName(AddOrgWindow)
    # setupUi

    def retranslateUi(self, AddOrgWindow):
        AddOrgWindow.setWindowTitle(QCoreApplication.translate("AddOrgWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("AddOrgWindow", u"Add New Organization", None))
        self.mainBox.setTitle(QCoreApplication.translate("AddOrgWindow", u"Organization Info", None))
        self.label_2.setText(QCoreApplication.translate("AddOrgWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("AddOrgWindow", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("AddOrgWindow", u"Phone", None))
        self.label_5.setText(QCoreApplication.translate("AddOrgWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("AddOrgWindow", u"Website", None))
#if QT_CONFIG(tooltip)
        self.emailField.setToolTip(QCoreApplication.translate("AddOrgWindow", u"Organization's Email Address", None))
#endif // QT_CONFIG(tooltip)
        self.addressBox.setTitle(QCoreApplication.translate("AddOrgWindow", u"Organization Address", None))
        self.label_7.setText(QCoreApplication.translate("AddOrgWindow", u"Street Address", None))
        self.label_8.setText(QCoreApplication.translate("AddOrgWindow", u"City", None))
        self.label_9.setText(QCoreApplication.translate("AddOrgWindow", u"State", None))
        self.label_10.setText(QCoreApplication.translate("AddOrgWindow", u"Country", None))
        self.label_11.setText(QCoreApplication.translate("AddOrgWindow", u"Zip Code", None))
        self.okButton.setText(QCoreApplication.translate("AddOrgWindow", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("AddOrgWindow", u"Cancel", None))
    # retranslateUi

