# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 770)
        MainWindow.setStyleSheet(u"background-color:#04395e;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.menuLayout = QVBoxLayout()
        self.menuLayout.setSpacing(6)
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.menuLayout.setContentsMargins(-1, 100, -1, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 0 5px;\n"
"border-radius:10px;\n"
"")

        self.menuLayout.addWidget(self.label)

        self.dashboardButton = QPushButton(self.centralwidget)
        self.dashboardButton.setObjectName(u"dashboardButton")
        self.dashboardButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"text-align: left\n"
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
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/resources/images/dashboard-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboardButton.setIcon(icon)
        self.dashboardButton.setIconSize(QSize(30, 30))

        self.menuLayout.addWidget(self.dashboardButton)

        self.organizationButton = QPushButton(self.centralwidget)
        self.organizationButton.setObjectName(u"organizationButton")
        self.organizationButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"text-align:left;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/images/resources/images/company-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.organizationButton.setIcon(icon1)
        self.organizationButton.setIconSize(QSize(32, 32))

        self.menuLayout.addWidget(self.organizationButton)

        self.employeeButton = QPushButton(self.centralwidget)
        self.employeeButton.setObjectName(u"employeeButton")
        self.employeeButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"text-align:left\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/images/resources/images/employee-contact-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.employeeButton.setIcon(icon2)
        self.employeeButton.setIconSize(QSize(40, 40))

        self.menuLayout.addWidget(self.employeeButton)

        self.salariesButton = QPushButton(self.centralwidget)
        self.salariesButton.setObjectName(u"salariesButton")
        self.salariesButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"text-align:left\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/images/resources/images/dollar-coin-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.salariesButton.setIcon(icon3)
        self.salariesButton.setIconSize(QSize(29, 29))

        self.menuLayout.addWidget(self.salariesButton)

        self.attendanceButton = QPushButton(self.centralwidget)
        self.attendanceButton.setObjectName(u"attendanceButton")
        self.attendanceButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"text-align:left\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/images/resources/images/fingerprint-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attendanceButton.setIcon(icon4)
        self.attendanceButton.setIconSize(QSize(32, 32))

        self.menuLayout.addWidget(self.attendanceButton)

        self.loanButton = QPushButton(self.centralwidget)
        self.loanButton.setObjectName(u"loanButton")
        self.loanButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"text-align:left\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/images/resources/images/calculator-desmos-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loanButton.setIcon(icon5)
        self.loanButton.setIconSize(QSize(32, 25))

        self.menuLayout.addWidget(self.loanButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.menuLayout.addItem(self.verticalSpacer)


        self.mainLayout.addLayout(self.menuLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame[frameShape=\"4\"] /* QFrame::HLine == 0x0004 */\n"
"{\n"
"    color: red;\n"
"}")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addWidget(self.line)

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.titlebarLayout = QHBoxLayout()
        self.titlebarLayout.setObjectName(u"titlebarLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titlebarLayout.addItem(self.horizontalSpacer_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"width:250px;\n"
"height: 25px;\n"
"margin: 3px 0;")

        self.titlebarLayout.addWidget(self.lineEdit)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
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

        self.titlebarLayout.addWidget(self.pushButton_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.titlebarLayout.addItem(self.horizontalSpacer)


        self.bodyLayout.addLayout(self.titlebarLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.bodyLayout.addWidget(self.line_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.employeeScreen = QWidget()
        self.employeeScreen.setObjectName(u"employeeScreen")
        self.verticalLayoutWidget = QWidget(self.employeeScreen)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 50, 312, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 0 5px;\n"
"border-radius:20px;\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayoutWidget_2 = QWidget(self.employeeScreen)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 150, 321, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 14px;\n"
"border-radius:20px;\n"
"")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalLayoutWidget_3 = QWidget(self.employeeScreen)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(359, 59, 758, 171))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 0 5px;\n"
"border-radius:10px;\n"
"")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.verticalLayoutWidget_4 = QWidget(self.employeeScreen)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(29, 279, 985, 301))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 0 5px;\n"
"border-radius:10px;\n"
"")

        self.verticalLayout_7.addWidget(self.label_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.employeeScreen)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayoutWidget = QWidget(self.page_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 221, 101))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.bodyLayout.addWidget(self.frame)

        self.bodyLayout.setStretch(2, 90)

        self.mainLayout.addLayout(self.bodyLayout)

        self.mainLayout.setStretch(2, 85)

        self.horizontalLayout_2.addLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HR-MS", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.organizationButton.setText(QCoreApplication.translate("MainWindow", u"Organizations", None))
#if QT_CONFIG(shortcut)
        self.organizationButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.employeeButton.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.salariesButton.setText(QCoreApplication.translate("MainWindow", u"Salaries", None))
        self.attendanceButton.setText(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.loanButton.setText(QCoreApplication.translate("MainWindow", u"Loans", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Our Successful Employees: 670", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Trusteb by 27+ Organizations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"For More Queries , contact us at +923001234567 or Email is at HR@Hrms.com", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Our employess salary graph:    setting kr lein apai ty ethy graph pa la", None))
    # retranslateUi

