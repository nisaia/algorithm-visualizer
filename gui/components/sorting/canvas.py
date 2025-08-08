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
        bar_width = w / len(visual_data)
        max_val = max(val for val, _ in visual_data)

        for i, (val, color) in enumerate(visual_data):
            x = i * bar_width
            bar_height = (val / max_val) * h
            y = h - bar_height

            # Ombra leggera
            painter.setPen(QColor(0, 0, 0, 40))
            painter.setBrush(color)

            # Barre arrotondate
            painter.drawRoundedRect(int(x), int(y), int(bar_width), int(bar_height), 5, 5)

    def set_speed(self, ms):
        self.timer.setInterval(ms)
