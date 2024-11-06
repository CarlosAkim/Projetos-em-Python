
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, 
                               QWidget, QVBoxLayout)
from main_class import MyClass
from display import Display
from info import Info
from buttons import MyButton, myGrid

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MyClass()
    
    # info
    info = Info('')
    window.addToVLayout(info)
    
    # Display
    display = Display()
    window.addToVLayout(display)  # Adicionando Display
    
    # Noss Grid
    buttonGrid = myGrid(display)
    window.vLayout.addLayout(buttonGrid) #a Adicionando o espaço do Layout
    
    
    
    
    
    
    
    
    # button = MyButton("Meu Botãozinho")
    # window.addToVLayout(button)
    
    # button2 = MyButton("Meu Botãozinho")
    # window.addToVLayout(button2)
    
    
    window.ajustFixaSize()
    window.show()
    
    
    app.exec()