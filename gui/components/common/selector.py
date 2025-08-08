from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import  QWidget, QGridLayout
from gui.components.common.card import Card

class Selector(QWidget):
    card_clicked_signal = pyqtSignal(str, list)

    def __init__(self, algorithm_classes: dict):
        super().__init__()

        layout = QGridLayout()
        row, col = 0, 0
        self.algorithm_classes = algorithm_classes

        for cls in self.algorithm_classes:

            name = cls.get("name")
            description = cls.get("description")
            image_path = cls.get("image_path")
            class_path = cls.get("class_path")
            algorithms = cls.get("algorithms")

            card = Card(name, image_path)
            f = lambda _, view_path=class_path, algorithms=algorithms: self.on_card_clicked(view_path, algorithms)
            card.clicked.connect(f)
            layout.addWidget(card, row, col)

            col += 1
            if col >= 3:
                col = 0
                row += 1

        self.setLayout(layout)

    def on_card_clicked(self, view_path, algorithms):
        print(f"Classe selezionata: {view_path}")

        self.card_clicked_signal.emit(view_path, algorithms)

        #if view_path is not None:
        #    AlgorithmView = load_class(view_path)
        #    algorithm_view = AlgorithmView(algorithms)
        #    algorithm_view.show()

        # Puoi aggiungere qui una logica per cambiare vista o avviare l'algoritmo
