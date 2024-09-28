from PySide6.QtWidgets import QLineEdit
import variable
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        # list comprehension para deixar todos os lados iguais
        margins = [variable.DEFAULT_TEXT_MARGIN for _ in range(4)] # type: ignore
        
        self.setStyleSheet(f"font-size: {variable.BIG_FONTE_SIZE}px")
        self.setMinimumHeight(variable.BIG_FONTE_SIZE * 2)
        self.setMinimumWidth(variable.MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)