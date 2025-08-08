from email.policy import default

from algorithms.core.base_algorithm import BaseAlgorithm
from PyQt6.QtGui import QColor

class BubbleSortAlgorithm(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.initialize()
    
    def initialize(self):
        self.i = 0
        self.j = 0

    def _step_impl(self) -> bool:
        # Logica semplificata del bubble sort
        if self.i < len(self.data) - 1:
            if self.j < len(self.data) - self.i - 1:
                if self.data[self.j] > self.data[self.j + 1]:
                    self.data[self.j], self.data[self.j + 1] = self.data[self.j + 1], self.data[self.j]
                self.j += 1
            else:
                self.j = 0
                self.i += 1
            return True
        else:
            return False

    def _get_state(self) -> dict:

        return {
            "data": self.data[:],
            "i": self.i,
            "j": self.j
        }

    def _set_state(self, state: dict):

        self.data = state["data"][:]
        self.i = state["i"]
        self.j = state["j"]

    def get_visual_state(self):

        default_color = QColor(200, 200, 200)

        if not self.started:
            return [(val, default_color) for val in self.data]

        visual = []
        for idx, val in enumerate(self.data):

            if idx > len(self.data) - self.i - 1:
                color = QColor(0, 255, 0)
            elif idx == self.j or idx == self.j + 1:
                if self.j + 1 < len(self.data):
                    if self.data[self.j] < self.data[self.j + 1]:
                        color = QColor(255, 0, 0) if idx == self.j else QColor(255, 80, 80)
                    else:
                        color = QColor(0, 150, 255) if idx == self.j else QColor(100, 200, 255)
                else:
                    color = default_color  # fuori dai limiti
            else:
                color = default_color

            visual.append((val, color))

        return visual

    def get_pseudocode(self) -> str:

        return """
        for i = 1 to n - 1
            for j = 1 to n - i
                if a[j] > a[j + 1] then
                    swap(a[j], a[j + 1])
        """
