from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variable import MEDIUM_FONTE_SIZE
from utils import isEmpty, notNumOrDot
from display import Display

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
    def __init__(self,display: Display, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent)
        
        self._gridMaks = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", "", ".", "="],
        ]
        self.display = display
        self._makeGrid() # Chama a função no iniciar
        
    # Função que adiciona os elementos ao grid
    def _makeGrid(self):
        for i, row in enumerate(self._gridMaks):
            for j, button_text in enumerate(row):
                # Ignora células vazias
                if button_text == "":
                    continue
                
                # Cria o botão com o texto correspondente
                button = MyButton(button_text)
                
                # Se o botão for '0', usa rowspan 2 e pula para o próximo item
                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2)
                    continue  # Vai para o próximo item, evitando que seja adicionado novamente

                # Adiciona o botão normalmente
                self.addWidget(button, i, j)
                
                button.clicked.connect(self._insertButtonTextDisplay) # comando que aciona quando clicar em valor na calculadora
    
    def _insertButtonTextDisplay(self, checked, button): # Função que fara o valor acionado aparecer no display
        self.display.setText("Cliked")
        print(123, checked, button.text())
