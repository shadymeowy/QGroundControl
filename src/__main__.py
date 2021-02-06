import sys
from PySide2.QtWidgets import *
    
try:
    from .mainwindow import MainWindow
except ImportError:
    from mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    r = app.exec_()
    main_window.cleanup()
    sys.exit(r)


if __name__ == "__main__":
    main()
