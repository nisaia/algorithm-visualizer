from PyQt6.QtGui import QColor
from algorithms.core.base_algorithm import BaseAlgorithm
from config.constants import GREEN

class SelectionSortAlgorithm(BaseAlgorithm):

    def initialize(self):
        self.i = 0
        self.j = self.i + 1
        self.min_idx = self.i
        # self._save_state()  # salva lo stato iniziale

    def _step_impl(self) -> bool:
        if self.i < len(self.data) - 1:
            if self.j < len(self.data):
                if self.data[self.j] < self.data[self.min_idx]:
                    self.min_idx = self.j
                self.j += 1
            else:
                # Scambia l'elemento corrente con il minimo trovato
                self.data[self.i], self.data[self.min_idx] = self.data[self.min_idx], self.data[self.i]
                self.i += 1
                self.j = self.i + 1
                self.min_idx = self.i
            return True
        return False

    def _get_state(self) -> dict:

        return {
            "data": self.data[:],  # copia profonda
            "i": self.i,
            "j": self.j,
            "min_idx": self.min_idx
        }

    def _set_state(self, state: dict):

        self.data = state["data"][:]
        self.i = state["i"]
        self.j = state["j"]
        self.min_idx = state["min_idx"]

    def get_visual_state(self):

        default_color = QColor(200, 200, 200)

        if not self.started:
            return [(val, default_color) for val in self.data]

        visual = []
        for idx, val in enumerate(self.data):

            if idx < self.i:
                color = QColor(*GREEN)
            elif idx == self.j:
                color = QColor(255, 0, 0)  # confronto
            elif idx == self.min_idx:
                color = QColor(0, 0, 255)  # minimo trovato
            else:
                color = default_color

            visual.append((val, color))

        return visual

    def get_pseudocode(self) -> str:
        return """
        for i = 0 to n - 1
            min = i
            for j = i + 1 to n
                if a[j] < a[min] then
                    min = j
            swap(a[i], a[min])
        """
