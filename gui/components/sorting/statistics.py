from PyQt6.QtWidgets import QWidget, QVBoxLayout


class Statistics(QWidget):

    def __init__(self):
        super.__init__()
        
        vertical_layout = QVBoxLayout()

        comparison_widget = QWidget()
        swap_widget = QWidget()

        vertical_layout.addWidget(comparison_widget)
        vertical_layout.addWidget(swap_widget)

        self.setLayout(vertical_layout)