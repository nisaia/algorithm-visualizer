from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

class Button(QPushButton):

    def __init__(
        self,
        text,
        parent=None,
        on_click=None
    ):
        super().__init__(text, parent)
        self.on_click=on_click
        self.clicked.connect(self.click)

        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(20)
        glow.setColor(QColor("#3fa18f"))
        glow.setOffset(0, 0)

        self.setGraphicsEffect(glow)

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def click(self):
        if self.on_click:
            self.on_click()   