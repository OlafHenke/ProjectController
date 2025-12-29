from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("ProjectController")
        self.resize(600, 400)

        self.btn_exit = QPushButton("Beenden")
        self.btn_exit.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_exit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
