from typing import List, Any
from algorithms.core.base_algorithm import BaseAlgorithm

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

    def get_visual_state(self) -> List[Any]:
        return self.data

    def get_pseudocode(self) -> str:

        return """
        
        """