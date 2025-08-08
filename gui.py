import sys, random
from PyQt6.QtWidgets import QApplication
from gui.views.main_view import MainWindow

def load_stylesheet(path):
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet("gui/assets/styles/theme.qss"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
