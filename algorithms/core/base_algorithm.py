from abc import ABC, abstractmethod, ABCMeta
from typing import List, Any
from PyQt6.QtCore import pyqtSignal, QObject

class MetaQObjectABC(type(QObject), ABCMeta):
    pass

class BaseAlgorithm(QObject, ABC, metaclass=MetaQObjectABC):

    started_signal = pyqtSignal()
    paused_signal = pyqtSignal()
    finished_signal = pyqtSignal()

    def __init__(self, name: str, data: Any) -> None:
        super().__init__()

        """
        Inizializza l'algoritmo con i dati da elaborare.
        :param data: Lista di elementi da visualizzare e manipolare.
        """

        self.name = name
        self.data = data
        self.steps = []
        self.current_step_index = -1
        self.started = False
        self.paused = False
        self.finished = False

    def get_name(self) -> str:
        return self.name

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.paused_signal.emit()

    def step(self) -> bool:

        if not self.started:
            self.started = True
            self.started_signal.emit()

        if self.paused:
            return True

        if self.current_step_index < len(self.steps) - 1:
            self.steps = self.steps[:self.current_step_index + 1]

        still_running = self._step_impl()

        if still_running:
            self._save_state(self._get_state())
            self.current_step_index += 1
        else:
            self.finished = True
            self.finished_signal.emit()

        return still_running

    @abstractmethod
    def initialize(self):

        """
        Prepara l'algoritmo per l'esecuzione (reset, setup iniziale).
        """

        pass

    @abstractmethod
    def _step_impl(self) -> bool:

        """
        Esegue un singolo passo dell'algoritmo.
        :return: True se ci sono ancora passi da eseguire, False se è finito.
        """

        pass

    @abstractmethod
    def get_visual_state(self) -> List[Any]:

        """
        Restituisce lo stato visualizzabile corrente (es. colori, posizioni).
        :return: Lista di elementi visuali aggiornati.
        """
        pass

    @abstractmethod
    def get_pseudocode(self) -> str:
        """
        Restituisce lo pseudocodice dell'algoritmo
        :return: String dello pseudocodice
        """

    def reset(self):

        """
        Resetta l'algoritmo allo stato iniziale.
        """

        self.current_step_index = 0
        self.started = False
        self.finished = False
        self.steps.clear()
        self.initialize()

    def is_finished(self) -> bool:
        return self.finished

    def is_started(self) -> bool:
        return self.started

    def step_back(self):

        if self.current_step_index > 0:
            self.current_step_index -= 1
            self._load_state(self.steps[self.current_step_index])
            return True
        return False

    def _save_state(self, state):
        self.steps.append(state)

    def _load_state(self, state):
        self._set_state(state)

    @abstractmethod
    def _get_state(self) -> dict:
        """
        Restituisce lo stato corrente dell'algoritmo (data, indici, ecc.)
        """
        pass

    @abstractmethod
    def _set_state(self, state: dict):
        """
        Imposta lo stato dell'algoritmo da un dizionario salvato
        """
        pass