from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from algorithms.searching.linear_search import LinearSearchAlgorithm
from gui.components.common.settings import Settings
from gui.components.searching.canvas import Canvas
from config.constants import MIN_BAR_HEIGHT, MAX_BAR_HEIGHT

from gui.utils.utils import load_class, get_unique_array, get_sorted_unique_array

class SearchingAlgorithmView(QMainWindow):

    def __init__(self, algorithms):
        super().__init__()

        self.algorithms = sorted(algorithms, key=lambda x: x.get("name"), reverse=False)

        # Default algorithm
        algorithm = self.algorithms[0]
        AlgorithmClass = load_class(algorithm.get("class_path"))

        name = algorithm.get("name")
        data = (
            get_unique_array(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT, 10)
            if isinstance(AlgorithmClass, LinearSearchAlgorithm)
            else get_sorted_unique_array(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT, 10)
        )
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

    def change_algorithm(self, algorithm_id: int):

        algorithm = list(filter(lambda x: x.get("id") == algorithm_id, self.algorithms))[0]

        algorithm_class_path = algorithm.get("class_path")
        AlgorithmClass = load_class(algorithm_class_path)

        name = algorithm.get("name")
        data = (
            get_unique_array(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT, len(self.algorithm.data))
            if isinstance(AlgorithmClass, LinearSearchAlgorithm)
            else get_sorted_unique_array(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT, len(self.algorithm.data))
        )

        self.algorithm = AlgorithmClass(name, data)
        self.algorithm.finished_signal.connect(self.reset)

        # self.code_viewer.load_code(self.algorithm.get_pseudocode())
        self.canvas.set_algorithm(self.algorithm)
        self.canvas.update()

    def change_array_elements_number(self, value):
        self.generate_new_array(value)

    def change_speed(self, value):
        self.canvas.set_speed(value)

    def generate_new_array(self, value: int):

        new_data = get_unique_array(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT, value)
        self.algorithm.data = new_data
        self.algorithm.reset()
        self.canvas.update()

    def start_algorithm(self, ms):
        self.canvas.start(ms)

    def pause_algorithm(self):
        self.canvas.stop()

    def reset(self):

        self.settings.reset_settings()
        # self.algorithm.reset()