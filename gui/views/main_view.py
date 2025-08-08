from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from gui.components.common.selector import Selector
from gui.utils.loader import load_class
import os
import json

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleziona un Algoritmo")
        self.stack = QStackedWidget()
        self.setGeometry(100, 100, 1000, 1000)

        current_dir = os.path.dirname(__file__)
        json_path = os.path.join(current_dir, "..", "..", "config", "algorithms.json")
        print(json_path)

        with open(os.path.abspath(json_path), "r") as f:
            algorithm_classes = json.load(f)

        self.selector = Selector(algorithm_classes)
        self.selector.card_clicked_signal.connect(self.switch_view)

        self.stack.addWidget(self.selector)
        self.setCentralWidget(self.stack)

    def switch_view(self, view_path, algorithms):
        print(f"Switching to view: {view_path}")

        AlgorithmView = load_class(view_path)
        algorithm_view = AlgorithmView(algorithms)

        self.stack.addWidget(algorithm_view)
        self.stack.setCurrentWidget(algorithm_view)
