from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QSlider


def respond_to_slider(data):
    print("Slider moved to: ", data)


def button_clicked(data):
    print("You clicked the button, didn't you! checked: ", data)


app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#button = QPushButton("Press Me")
# button.setCheckable(True)
# button.clicked.connect(button_clicked)
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
