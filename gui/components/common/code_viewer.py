from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QVBoxLayout, QPushButton


class CodeViewer(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.code_viewer = QPlainTextEdit()
        self.code_viewer.setMaximumWidth(500)
        self.code_viewer.setMaximumHeight(300)

        self.code_viewer.setReadOnly(True)
        self.code_viewer.setFont(QFont("Courier"))
        self.code_viewer.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.toggle_button = QPushButton("Mostra/Nascondi Codice")
        self.toggle_button.clicked.connect(lambda: self.code_viewer.setVisible(not self.code_viewer.isVisible()))

        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.code_viewer)
        self.setLayout(layout)

    def load_code(self, pseudo_code: str) -> None:
        self.code_viewer.setPlainText(pseudo_code)

