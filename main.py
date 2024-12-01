import sys
import random
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.circles = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Circle Drawer')
        self.setGeometry(100, 100, 800, 600)

        self.pushButton = QtWidgets.QPushButton('Добавить окружность', self)
        self.pushButton.setGeometry(100, 100, 200, 100)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for diameter, color in self.circles:
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
