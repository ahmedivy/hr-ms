import sys
import time
from PySide6.QtCore import Slot
from ui.message_ui import Ui_messageLabel
from ui.mainwindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.on_login)

    @Slot()
    def on_login(self):
        self.email = self.ui.emailLineEdit.text()
        self.password = self.ui.passwordLineEdit.text()
        if not self.email or not self.password:
            self.ui.validationLabel.setText("Please enter email and password")
        if self.email == "admin" and self.password == "admin":
            self.ui.validationLabel.setText("Login Successful")
            self.ui.messageLabel = MessageLabel()
            self.ui.messageLabel.show()
            time.sleep(5)
            self.ui.messageLabel.close()
        else:
            self.ui.validationLabel.setText("Invalid email or password")

        self.ui.emailLineEdit.clear()
        self.ui.passwordLineEdit.clear()


class MessageLabel(QDialog):
    def __init__(self):
        super(MessageLabel, self).__init__()
        self.ui = Ui_messageLabel()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Login")
    window.show()

    sys.exit(app.exec())
