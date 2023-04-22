from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()


        distance_label = QLabel("Distance:")
        self.distance_ledit = QLineEdit()

        time_label = QLabel("Times(hours):")
        self.time_ledit = QLineEdit()

        self.combobox = QComboBox()
        self.combobox.addItems(["Metrics(km)", "Imperial(miles)"])

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel(" ")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_ledit, 0, 1)
        grid.addWidget(self.combobox, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_ledit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_ledit.text())
        time = float(self.time_ledit.text())

        speed = distance / time

        if self.combobox.currentText() == "Metrics(km)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.combobox.currentText() == "Imperial(miles)":
            speed = round(speed * 0.621271, 2)
            unit = "mph"

        self.output_label.setText(f" AVERAGE SPEED: {speed}{unit}")


app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())
