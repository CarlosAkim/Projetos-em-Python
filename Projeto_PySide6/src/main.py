
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
    info = Info('teste')
    window.addToVLayout(info)
    
    # Display
    display = Display()
    window.addToVLayout(display)  # Adicionando Display
    
    # Noss Grid
    buttonGrid = myGrid()
    window.vLayout.addLayout(buttonGrid) #a Adicionando o espaço do Layout
    buttonGrid.addWidget(MyButton("0"), 0, 0) # adicionando os buttons
    buttonGrid.addWidget(MyButton("1"), 0, 1)
    buttonGrid.addWidget(MyButton("2"), 0, 2)
    buttonGrid.addWidget(MyButton("3"), 1, 0)
    
    
    
    
    
    
    
    # button = MyButton("Meu Botãozinho")
    # window.addToVLayout(button)
    
    # button2 = MyButton("Meu Botãozinho")
    # window.addToVLayout(button2)
    
    
    window.ajustFixaSize()
    window.show()
    
    
    app.exec()