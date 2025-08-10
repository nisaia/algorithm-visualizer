from PyQt6.QtWidgets import QComboBox, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

class ComboBox(QWidget):

    def __init__(
        self,
        label,
        values,
        parent=None,
        on_value_change=None
    ):
        super().__init__(parent)

        self.label = QLabel(label)
        self.combo_box = QComboBox()
        self.combo_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.on_value_change=on_value_change
        
        for value in values:
            self.combo_box.addItem(value)

        self.combo_box.currentIndexChanged.connect(lambda x: self.value_changed(self.combo_box.currentIndex()))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)
        self.setLayout(layout)

    def value_changed(self, value):

        if self.on_value_change:
            self.on_value_change(value)