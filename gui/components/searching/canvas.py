from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QLinearGradient
from PyQt6.QtCore import QTimer

from algorithms.searching.linear_search import LinearSearchAlgorithm


class Canvas(QWidget):

    def __init__(self, algorithm):
        super().__init__()
        self.algorithm = algorithm

        self.timer = QTimer()
        self.timer.timeout.connect(self.run_step)

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def start(self, ms):
        self.algorithm.initialize()
        # self.algorithm.started = True
        self.algorithm.step()
        self.timer.start(ms) # 100 ms tra i passi

    def stop(self):
        self.algorithm.step()
        self.timer.stop()

    def run_step(self):
        if self.algorithm.step():
            self.update()  # forza repaint
        else:
            self.timer.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        visual_data = self.algorithm.get_visual_state()
        if not visual_data:
            return

        print(*map(lambda x: x[0], visual_data))
        if isinstance(self.algorithm, LinearSearchAlgorithm):
            print(self.algorithm.key)

        w = self.width()
        h = self.height()
        spacing = 10  # spazio tra quadrati
        num_items = len(visual_data)

        # Calcolo dimensioni quadrati
        total_spacing = spacing * (num_items - 1)
        max_square_size = min((w - total_spacing) / num_items, h * 0.6)
        square_size = int(max_square_size)

        # Calcolo margine per centrare orizzontalmente
        total_width = num_items * square_size + total_spacing
        start_x = (w - total_width) / 2
        y = (h - square_size) / 2

        # Font centrato nel quadrato
        font_size = max(8, int(square_size * 0.3))
        font = painter.font()
        font.setPointSize(font_size)
        painter.setFont(font)

        for i, (val, color) in enumerate(visual_data):
            x = start_x + i * (square_size + spacing)

            # Disegna quadrato
            painter.setPen(QColor(255, 255, 255, 40))
            painter.setBrush(color)
            painter.drawRoundedRect(int(x), int(y), square_size, square_size, 6, 6)

            # Disegna numero centrato
            painter.setPen(QColor(255, 255, 255))
            text = str(val)
            text_width = painter.fontMetrics().horizontalAdvance(text)
            text_height = painter.fontMetrics().height()
            text_x = int(x + (square_size - text_width) / 2)
            text_y = int(y + (square_size + text_height) / 2) - 4

            painter.drawText(text_x, text_y, text)

    def set_speed(self, ms):
        self.timer.setInterval(ms)
