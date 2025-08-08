from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtCore import pyqtSignal, Qt

class Card(QWidget):
    clicked = pyqtSignal(str)

    def __init__(self, name: str, image_path: str):
        super().__init__()
        self.name = name
        self.image_path = image_path

        self.image_label = QLabel()
        self.normal_pixmap = QPixmap(image_path).scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio)
        self.hover_pixmap = QPixmap(image_path).scaled(140, 140, Qt.AspectRatioMode.KeepAspectRatio)

        self.image_label.setPixmap(self.normal_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.text_label = QLabel(name)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)
        self.setLayout(layout)

        # Abilita eventi di hover
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

    def enterEvent(self, event):
        self.image_label.setPixmap(self.hover_pixmap)

    def leaveEvent(self, event):
        self.image_label.setPixmap(self.normal_pixmap)

    def mousePressEvent(self, event: QMouseEvent):
        self.clicked.emit(self.name)
