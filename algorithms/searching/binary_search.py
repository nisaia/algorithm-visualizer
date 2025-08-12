import random
from typing import List, Any

from PyQt6.QtGui import QColor
from config.constants import GRAY

from algorithms.core.base_algorithm import BaseAlgorithm

class BinarySearchAlgorithm(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)
        self.initialize()

    def initialize(self):
        self.mid = len(self.data) // 2
        self.key = self.data[random.randint(0, len(self.data) - 1)]

    def _step_impl(self) -> bool:
        pass

    def _get_state(self) -> dict:

        return {
            "data": self.data[:],
            "mid": self.mid,
            "key": self.key
        }

    def _set_state(self, state: dict):

        self.data = state["data"][:]
        self.mid = state["mid"]
        self.key = state["key"]

    def get_visual_state(self) -> List[Any]:

        return [(val, QColor(*GRAY)) for val in self.data]

    def get_pseudocode(self) -> str:

        return """
        
        """