from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from gui.components.common.settings import Settings
from gui.components.searching.canvas import Canvas

from gui.utils.loader import load_class
import random

class SearchingAlgorithmView(QMainWindow):

    def __init__(self, algorithms):
        super().__init__()

        self.setFixedSize(1000, 1000)

        self.algorithms = sorted(algorithms, key=lambda x: x.get("name"), reverse=False)

        # Default algorithm
        algorithm = self.algorithms[0]
        name, data = algorithm.get("name"), [random.randint(10, 100) for _ in range(10)]

        AlgorithmClass = load_class(algorithm.get("class_path"))
        self.algorithm = AlgorithmClass(name, data)

        self.algorithm.finished_signal.connect(self.reset)

        # Layout centrale
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.settings = Settings(self.algorithm, self.algorithms)

        self.settings.changed_algorithm_signal.connect(self.change_algorithm)
        self.settings.change_array_elements_number_signal.connect(self.change_array_elements_number)
        self.settings.change_speed_signal.connect(self.change_speed)

        self.settings.generate_array_signal.connect(self.generate_new_array)
        self.settings.started_algorithm_signal.connect(self.start_algorithm)
        self.settings.paused_algorithm_signal.connect(self.pause_algorithm)

        layout.addWidget(self.settings)

        # self.statistics = Statistics()
        # layout.addWidget(self.statistics)

        # Canvas per disegno
        self.canvas = Canvas(self.algorithm)
        layout.addWidget(self.canvas)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_array_elements_number(self, value):
        self.generate_new_array(value)

    def change_speed(self, value):
        # self.canvas.set_speed(value)
        pass

    def generate_new_array(self, value: int):

        new_data = [random.randint(1, 100) for _ in range(value)]
        self.algorithm.reset()
        self.algorithm.data = new_data
        self.canvas.update()

    def start_algorithm(self, ms):
        # self.canvas.start(ms)
        pass

    def pause_algorithm(self):
        # self.canvas.stop()
        pass

    def reset(self):

        self.settings.reset_settings()
        # self.algorithm.reset()