from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from gui.components.common.code_viewer import CodeViewer
from gui.components.common.settings import Settings
from gui.components.sorting.canvas import Canvas
from gui.utils.loader import load_class

from config.constants import MIN_BAR_HEIGHT, MAX_BAR_HEIGHT
import random

class SortingAlgorithmView(QMainWindow):

    def __init__(self, algorithms):
        super().__init__()
        # self.setWindowTitle(algorithm.get_name())

        self.algorithms = sorted(algorithms, key=lambda x: x.get("name"), reverse=False)

        # Default algorithm
        algorithm = self.algorithms[0]
        name, data = algorithm.get("name"), [random.randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT) for _ in range(30)]

        AlgorithmClass = load_class(algorithm.get("class_path"))
        self.algorithm = AlgorithmClass(name, data)

        self.algorithm.finished_signal.connect(self.reset)

        # Layout centrale
        central_widget = QWidget()
        layout = QVBoxLayout()
        # layout.setSpacing(50)  # Spazio verticale tra i widget
        # layout.setContentsMargins(100, 100, 10, 10)  # Margini esterni (sinistra, sopra, destra, sotto)

        self.settings = Settings(self.algorithm, self.algorithms)

        self.settings.changed_algorithm_signal.connect(self.change_algorithm)
        self.settings.change_array_elements_number_signal.connect(self.change_array_elements_number)
        self.settings.change_speed_signal.connect(self.change_speed)

        self.settings.generate_array_signal.connect(self.generate_new_array)
        self.settings.started_algorithm_signal.connect(self.start_algorithm)
        self.settings.paused_algorithm_signal.connect(self.pause_algorithm)

        layout.addWidget(self.settings)

        #self.statistics = Statistics()
        #layout.addWidget(self.statistics)

        #self.code_viewer = CodeViewer()
        #self.code_viewer.load_code(self.algorithm.get_pseudocode())
        #layout.addWidget(self.code_viewer)

        # Canvas per disegno
        self.canvas = Canvas(self.algorithm)
        layout.addWidget(self.canvas)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_algorithm(self, algorithm_id: int):

        algorithm = list(filter(lambda x: x.get("id") == algorithm_id, self.algorithms))[0]

        name, data = algorithm.get("name"), [random.randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT) for _ in range(len(self.algorithm.data))]

        algorithm_class_path = algorithm.get("class_path")
        AlgorithmClass = load_class(algorithm_class_path)

        self.algorithm = AlgorithmClass(name, data)
        self.algorithm.finished_signal.connect(self.reset)

        # self.code_viewer.load_code(self.algorithm.get_pseudocode())
        self.canvas.set_algorithm(self.algorithm)

    def change_array_elements_number(self, value):
        self.generate_new_array(value)

    def change_speed(self, value):
        self.canvas.set_speed(value)

    def generate_new_array(self, value: int):

        new_data = [random.randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT) for _ in range(value)]
        self.algorithm.reset()
        self.algorithm.data = new_data
        self.canvas.update()

    def start_algorithm(self, ms):
        self.canvas.start(ms)

    def pause_algorithm(self):
        self.canvas.stop()

    def reset(self):

        self.settings.reset_settings()
        # self.algorithm.reset()
