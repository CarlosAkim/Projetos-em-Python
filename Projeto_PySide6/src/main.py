
import sys
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, 
                               QWidget, QVBoxLayout)
from main_class import MyClass
from display import Display

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MyClass()
    
    # ACESSANDO ITENS FORA DA CLASSE
    # label1 = QLabel("Minha janela")
    # label1.setStyleSheet("font-size: 50px;")
    # window.addToVLayout(label1)
    
    # Display
    display = Display()
    
    # Adicionando Display
    window.addToVLayout(display)
    window.addToVLayout(Display("display 2"))
    window.addToVLayout(Display('display 3'))
    
    
    
    window.ajustFixaSize()
    window.show()
    
    
    app.exec()