from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QLinearGradient
from PyQt6.QtCore import QTimer

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

        w = self.width()
        h = self.height()
        spacing = 1
        num_bars = len(visual_data)

        total_spacing = spacing * (num_bars - 1)
        bar_width = (w - total_spacing) / num_bars
        max_val = max(val for val, _ in visual_data)

        font_size = max(3, int(bar_width * 0.3))
        font = painter.font()
        font.setPointSize(font_size)
        painter.setFont(font)

        font_height = painter.fontMetrics().height()
        top_margin = font_height + 5
        usable_height = h - top_margin

        for i, (val, color) in enumerate(visual_data):
            x = i * (bar_width + spacing)
            bar_height = (val / max_val) * usable_height
            y = h - bar_height

            painter.setPen(QColor(0, 0, 0, 40))
            painter.setBrush(color)
            painter.drawRoundedRect(int(x), int(y), int(bar_width), int(bar_height), 5, 5)

            painter.setPen(QColor(255, 255, 255))
            text = str(val)
            text_width = painter.fontMetrics().horizontalAdvance(text)
            text_x = int(x + (bar_width - text_width) / 2)
            text_y = int(y) - 10

            if text_y < font_height:
                text_y = font_height

            painter.drawText(text_x, text_y, text)

    def set_speed(self, ms):
        self.timer.setInterval(ms)
