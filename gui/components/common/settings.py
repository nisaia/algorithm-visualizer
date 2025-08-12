from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from gui.components.common.slider import Slider
from gui.components.common.combo_box import ComboBox
from gui.components.common.button import Button

class Settings(QWidget):

    changed_algorithm_signal = pyqtSignal(int)
    change_array_elements_number_signal = pyqtSignal(int)
    change_speed_signal = pyqtSignal(int)

    started_algorithm_signal = pyqtSignal(int)
    paused_algorithm_signal = pyqtSignal()
    finished_algorithm_signal = pyqtSignal()

    generate_array_signal = pyqtSignal(int)

    def __init__(self, algorithm, algorithms):
        super().__init__()

        self.algorithm = algorithm
        self.algorithms = algorithms

        algorithm_names = list(map(lambda x: x.get("name"), self.algorithms))

        #self.algorithm.started_signal.connect(self.started_control_buttons)
        #self.algorithm.paused_signal.connect(self.paused_control_buttons)
        #self.algorithm.finished_signal.connect(self.finished_control_buttons)

        vertical_layout = QVBoxLayout()
        
        self.combo_box = ComboBox("Algorithms", algorithm_names, on_value_change=self.change_algorithm)
        self.elements_slider = Slider(10, 100, 10,300, 10, "Elements", on_change=self.update_elements)
        self.speed_slider = Slider(50, 500, 10, 300, 10, "Speed", on_change=self.set_speed)

        layout = QHBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.elements_slider)
        layout.addWidget(self.speed_slider)
        
        self.generate_array_button = Button("Generate array", on_click=lambda: self.update_elements(self.elements_slider.get_slider_value()))
        self.start_button = Button("Start", on_click=lambda: self.start_algorithm(self.speed_slider.get_slider_value()))
        self.pause_button = Button("Pause", on_click=self.pause_algorithm)
        self.pause_button.setDisabled(True)
        
        layout_2 = QHBoxLayout()
        layout_2.addWidget(self.generate_array_button)
        layout_2.addWidget(self.start_button)
        layout_2.addWidget(self.pause_button)

        vertical_layout.addLayout(layout)
        vertical_layout.addLayout(layout_2)

        self.setLayout(vertical_layout)

    def start_algorithm(self, ms):

        self.combo_box.setDisabled(True)
        self.elements_slider.setDisabled(True)

        self.generate_array_button.setDisabled(True)
        self.start_button.setDisabled(True)
        self.pause_button.setEnabled(True)

        self.started_algorithm_signal.emit(ms)

    def pause_algorithm(self):

        self.algorithm.toggle_pause()

        if self.algorithm.paused:
            self.pause_button.setText("Resume")
            self.generate_array_button.setEnabled(True)
            self.start_button.setEnabled(True)
        else:
            self.pause_button.setText("Pausa")
            self.algorithm.step()

        self.paused_algorithm_signal.emit()

    def reset_settings(self):

        self.combo_box.setEnabled(True)

        self.elements_slider.setEnabled(True)
        # self.elements_slider.reset()
        # self.speed_slider.reset()

        self.generate_array_button.setEnabled(True)
        self.start_button.setDisabled(True)
        self.pause_button.setDisabled(True)

    def update_elements(self, value):

        if not self.start_button.isEnabled():
            self.start_button.setEnabled(True)

        self.generate_array_signal.emit(value)

    def set_speed(self, ms):
        #self.canvas.set_speed(ms)
        self.change_speed_signal.emit(ms)

    def change_algorithm(self, value: int):
        self.changed_algorithm_signal.emit(value)