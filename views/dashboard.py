from PySide6.QtWidgets import QWidget

from ui.widgets.dashboard_ui import Ui_DashboardWidget


class DashboardWidget(QWidget):
    def __init__(self):
        super(DashboardWidget, self).__init__()
        self.ui = Ui_DashboardWidget()
        self.ui.setupUi(self)
        
        self.setup_widgets()
        
    def setup_widgets(self):
        ...

