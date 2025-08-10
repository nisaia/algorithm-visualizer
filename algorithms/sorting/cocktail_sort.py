from typing import List, Any

from PyQt6.QtGui import QColor

from algorithms.core.base_algorithm import BaseAlgorithm
from config.constants import  GRAY, GREEN, RED

class CocktailSortAlgorithm(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.initialize()

    def initialize(self):
        self.start = 0
        self.end = len(self.data) - 1
        self.i = self.start
        self.forward = True
        self.swapped = True
        self.cycle_started = True
        self.finished = False

    def _step_impl(self) -> bool:

        if self.finished:
            return False

        if self.cycle_started:
            self.swapped = False
            self.cycle_started = False

        if self.forward:
            if self.i < self.end:
                if self.data[self.i] > self.data[self.i + 1]:
                    self.data[self.i], self.data[self.i + 1] = self.data[self.i + 1], self.data[self.i]
                    self.swapped = True
                self.i += 1
                return True
            else:
                self.end -= 1
                self.i = self.end
                self.forward = False
                self.cycle_started = True
                return True
        else:
            if self.i > self.start:
                if self.data[self.i - 1] > self.data[self.i]:
                    self.data[self.i - 1], self.data[self.i] = self.data[self.i], self.data[self.i - 1]
                    self.swapped = True
                self.i -= 1
                return True
            else:
                self.start += 1
                self.i = self.start
                self.forward = True
                self.cycle_started = True

                if not self.swapped:
                    self.finished = True
                    return False

                return True

    def _get_state(self) -> dict:

        return {
            "data": self.data[:],
            "start": self.start,
            "end": self.end
        }

    def _set_state(self, state: dict):

        self.data = state["data"][:]
        self.start = state["start"]
        self.end = state["end"]

    def get_visual_state(self) -> List[Any]:
        default_color = QColor(*GRAY)
        visual = []

        if not self.started:
            return [(val, default_color) for val in self.data]

        for idx, val in enumerate(self.data):
            if idx < self.start or idx > self.end:
                color = QColor(*GREEN)
            elif idx == self.i:
                color = QColor(*RED)
            else:
                color = default_color

            visual.append((val, color))

        return visual

    def get_pseudocode(self) -> str:

        return """"""