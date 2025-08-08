from PyQt6.QtWidgets import QPushButton

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

    def click(self):
        if self.on_click:
            self.on_click()   