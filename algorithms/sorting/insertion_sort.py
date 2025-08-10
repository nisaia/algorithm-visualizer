from typing import List, Any

from PyQt6.QtGui import QColor

from algorithms.core.base_algorithm import BaseAlgorithm
from config.constants import GRAY, GREEN, RED

class InsertionSortAlgorithm(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)

    def initialize(self):
        self.i = 1
        self.j = self.i - 1
        self.key = self.data[self.i]

    def _step_impl(self) -> bool:

        if self.j >= 0 and self.data[self.j] > self.key:

            self.data[self.j + 1] = self.data[self.j]
            self.j -= 1
            return False

        else:

            self.data[self.j + 1] = self.key
            self.i += 1
            if self.i < len(self.data):
                self.key = self.data[self.i]
                self.j = self.i - 1

        return True  # Continua l'ordinamento

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

    def get_visual_state(self) -> List[Any]:

        default_color = QColor(*GRAY)

        if not self.started:
            return [(val, default_color) for val in self.data]

        visual = []
        for idx, val in enumerate(self.data):

            if idx < self.i:
                color = QColor(*GREEN)
            elif idx == self.j:
                color = QColor(*RED)
            else:
                color = default_color

            visual.append((val, color))

        return visual

    def get_pseudocode(self) -> str:

        return """
        for i = 1 to n - 1
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = key
        """