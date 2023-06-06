from PySide6.QtWidgets import QDialog

from ui.dialogs.okDialog_ui import Ui_Dialog

class OkDialog(QDialog):
    def __init__(self, message: str, title: str,  parent=None):
        super(OkDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.message.setText(message)
        self.setWindowTitle(title)
        
        