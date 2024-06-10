# from urllib.request import urlopen
# from PIL import Image

# url = "https://www.tutorialspoint.com/images/logo.png"
# img = Image.open(urlopen(url))
# img.show()

from PySide6.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QFileDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QPainter, QPixmap, QShortcut

import sys

from typing import Optional

from PIL import Image


class Window(QGraphicsView):
    def __init__(self) -> None:
        super().__init__()

        self.path: Optional[str] = None

        self.resize(1000, 600)

        self.setScene(QGraphicsScene(self))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # self.setRenderHint(QPainter.Antialiasing, True)
        # self.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        self.setCursor(Qt.CursorShape.CrossCursor)

        QShortcut("Ctrl+W", self).activated.connect(self.set_chosen_image)
        QShortcut("Ctrl+D", self).activated.connect(self.toggle_drag_mode)
    
    def mouseMoveEvent(self, event):
        self.scene_pos = self.mapToScene(event.pos())

        super().mouseMoveEvent(event)
    
    def get_color_of_pos(self):
        if self.dragMode() == QGraphicsView.DragMode.NoDrag:
            image = Image.open(self.path)
            pixel_color = image.getpixel(self.mapToScene(self.cursor().pos()).toTuple())

            print("rgb" + str(pixel_color))
            # print("rgb" + str(pixel_color), "#" + "".join(map(lambda x: str(hex(x)).strip("0x"), pixel_color)))
    
    def set_chosen_image(self) -> None:

        self.path = QFileDialog.getOpenFileName(filter="ImageFiles (*.png *.jpg *.jpeg *.gif)")[0]
        self.scene().clear()

        self.pixmap = QPixmap(self.path)
        self.scene().addPixmap(self.pixmap)
    
    def toggle_drag_mode(self) -> None:
        if self.dragMode() == QGraphicsView.DragMode.NoDrag:
            self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

        elif self.dragMode() == QGraphicsView.DragMode.ScrollHandDrag:
            self.setDragMode(QGraphicsView.DragMode.NoDrag)
            self.setCursor(Qt.CursorShape.CrossCursor)
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self.dragMode() == QGraphicsView.DragMode.NoDrag and event.button() == Qt.MouseButton.LeftButton:
            self.get_color_of_pos()
        
        else:
            super().mousePressEvent(event)
    
    def wheelEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            factor = 1.2

            if event.angleDelta().y() < 0:
                factor = 1.0 / factor

            self.scale(factor, factor)

        else:
            super().wheelEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
