import sys
from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow
from logic.app_controller import AppController

def main():
    app = QApplication(sys.argv)

    controller = AppController()
    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
