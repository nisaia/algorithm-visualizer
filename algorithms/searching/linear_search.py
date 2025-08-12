import random
from typing import List, Any
from config.constants import GRAY, GREEN, RED

from PyQt6.QtGui import QColor

from algorithms.core.base_algorithm import BaseAlgorithm


class LinearSearchAlgorithm(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.initialize()

    def initialize(self):
        self.i = 0
        self.key = self.data[random.randint(0, len(self.data) - 1)]

    def _step_impl(self) -> bool:

        if self.i >= len(self.data) - 1 or self.data[self.i] == self.key:
            return False

        self.i += 1

        return True

    def _get_state(self) -> dict:

        return {
            "data": self.data[:],
            "i": self.i,
            "key": self.key
        }

    def _set_state(self, state: dict):

        self.data = state["data"][:]
        self.i = state["i"]
        self.key = state["key"]

    def get_visual_state(self) -> List[Any]:

        default_color = QColor(*GRAY)

        if not self.started:
            return [(val, default_color) for val in self.data]

        visual = []
        for idx, val in enumerate(self.data):

            if val == self.key and self.finished:
                color = QColor(*GREEN)
            elif idx == self.i:
                color = QColor(*RED)
            else:
                color = default_color

            visual.append((val, color))

        return visual

    def get_pseudocode(self) -> str:

        return """
        
        """