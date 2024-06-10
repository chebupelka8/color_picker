# from urllib.request import urlopen
# from PIL import Image

# url = "https://www.tutorialspoint.com/images/logo.png"
# img = Image.open(urlopen(url))
# img.show()

from PySide6.QtWidgets import (
    QApplication, QWidget
)
from PySide6.QtCore import Qt
# from PySide6.QtGui import QMouseEvent, QPainter, QPixmap, QShortcut

import sys

from typing import Optional

# from PIL import Image


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(1000, 600)
        # self.resize(1000, 600)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
