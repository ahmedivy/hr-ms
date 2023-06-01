import sys
from PySide6.QtWidgets import QApplication
from qdarktheme import setup_theme as apply_css

from views.login import LoginWindow
from views.addEmployee import AddEmployeeWindow

if __name__ == "__main__":
    # qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    
    apply_css("auto")
    
    window = AddEmployeeWindow()
    window.show()
    app.exec() 
    
