from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variable import MEDIUM_FONTE_SIZE

class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configButton()
        
        
    def configButton(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONTE_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')
        
class myGrid(QGridLayout):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent)