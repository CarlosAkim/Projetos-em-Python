from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QVBoxLayout, QLabel)
class MyClass(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # CRIAMOS UMA JANELA
        self.cW = QWidget()
        self.vLayout = QVBoxLayout()
        self.cW.setLayout(self.vLayout)
    
        # CRIAMOS UM LAYOUT
        self.setCentralWidget(self.cW)
        
        # DEFINIMOS UM TITULO PARA A JANELA    
        self.setWindowTitle("Minha Calculadora")
        
        # # CRIANDO O PRIMEIRO DOCUMENTO
        # self.label1 = QLabel("O meu texto") 
        # self.v_layout.addWidget(self.label1) #Adiciona elementos
          
        
    # FIXANDO O TAMANHO DA JANELA
    def ajustFixaSize(self):
        ...
        #self.setFixedSize(self.width(), self.height()) # Fixa o tamanho da janela
        #self.adjustSize() # ajusta o conteudo
    
    # Criamos uma função para encurtar a chamada do metodo.
    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)