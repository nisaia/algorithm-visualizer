from PyQt6.QtWidgets import QSlider, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class Slider(QWidget):

    def __init__(
        self,
        _min: int,
        _max: int,
        single_step: int,
        w: int,
        h: int,
        label: str,
        orientation=Qt.Orientation.Horizontal,
        parent=None,
        on_change=None,
        on_press=None,
        on_release=None,
        on_move=None
    ):
        super().__init__(parent)

        self._min = _min
        self._max = _max
        self.single_step = single_step
        self.w = w
        self.h = h

        self.on_change=on_change
        self.on_press=on_press
        self.on_release=on_release
        self.on_move=on_move

        self.label = QLabel(f"{label}: {_min}")
        self.label.setStyleSheet("font-size: 12px; margin-bottom: 0px;")
        self.label.setFixedHeight(16)

        self.slider = QSlider(orientation=orientation)
        self.slider.setRange(_min, _max)
        self.slider.setValue(_min)
        self.slider.setSingleStep(single_step)
        self.slider.setFixedSize(w, h)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.slider.valueChanged.connect(lambda val: self.value_changed(label, val))
        # self.slider.sliderMoved.connect(self.slider_position)
        # self.slider.sliderPressed.connect(self.slider_pressed)
        # self.slider.sliderReleased.connect(self.slider_released)

    def get_slider_value(self):
        return self.slider.value()

    def value_changed(self, label, value):
        self.label.setText(f"{label}: {value}")
        if self.on_change:
            self.on_change(value)

    #def slider_position(self, p):
    #    print("position", p)

    #def slider_pressed(self):
    #    print("Pressed!")

    #def slider_released(self):
    #    print("Released")

    def reset(self):
        self.slider.setValue(self._min)