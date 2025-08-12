from typing import List, Any

from algorithms.core.base_algorithm import BaseAlgorithm


class InterpolationSearchAlgorithm(BaseAlgorithm):

    def __init__(self, name, data):
        super().__init__(name, data)

    def initialize(self):
        pass

    def _step_impl(self) -> bool:
        pass

    def _get_state(self) -> dict:
        pass

    def _set_state(self, state: dict):
        pass

    def get_visual_state(self) -> List[Any]:
        pass

    def get_pseudocode(self) -> str:
        pass