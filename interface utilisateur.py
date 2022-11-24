import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        self.__nom = QLabel("")
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.__text, 1, 0)
        grid.addWidget(ok, 2, 0)
        grid.addWidget(quit, 2, 1)
        grid.addWidget(self.__nom, 3, 0)

        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Une première fenêtre")
    def __actionOk(self):
        prenom = self.__text.text()
        self.__nom.setText(f"bonjour {prenom}")

    def __actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    sys.exit(app.exec_())