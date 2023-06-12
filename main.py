import sys
from PySide6.QtWidgets import QApplication

from views.mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    app.exec() 
    
