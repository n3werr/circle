import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        self.circles.append(diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for diameter in self.circles:
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
