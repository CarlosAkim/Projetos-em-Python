import flet as ft

# Container personalizado
class MeuConteiner(ft.Container):
    def __init__(self, image_url, id, on_click = None):
        # Inicializa o Container com as propriedades básicas
        super().__init__()
        self.on_click = on_click
        self.height = 80
        self.width = 100
        self.border_radius = 15
        self.alignment = ft.alignment.center
        self.content = ft.Image(src=image_url)
        self.opacity = 1.0
        self.id = id
        if on_click:
            self.on_click = lambda e: on_click(id)
            
        @property    
        def opacity(self)-> float:
            return self.opacity
        
        @opacity.setter
        def opacity(self, porcentagem: float):
            self.opacity = porcentagem
            

def jogar(container_id):
    print(container_id)
    # Baixando a opacity de papel e pedra
    if container_id == 'pedra_jogador':
        papel_player.opacity(0.5)
        tesoura_player.opacity(0.5)
    elif container_id == 'papel_jogador':
        ...
    elif container_id == 'tesoura_jogador':
        ...
pedra_img = "imagems jokepo/pedra.png"
papel_img = "imagems jokepo/papel.png"
tesoura_img = "imagems jokepo/tesoura.png"

# Cria instâncias do MeuConteiner com imagens
pedra_maquina = MeuConteiner(image_url= pedra_img, id="pedra_maquina")
papel_maquina = MeuConteiner(image_url= papel_img, id="papel_maquina")
tesoura_maquina = MeuConteiner(image_url= tesoura_img, id='tesoura_maquina')

# Cria instância do MeuContainer para o usuario
pedra_player = MeuConteiner(image_url=pedra_img, id='pedra_jogador', on_click=jogar )
papel_player = MeuConteiner(image_url=papel_img, id="papel_jogador",on_click=jogar )
tesoura_player = MeuConteiner(image_url=tesoura_img, id='tesoura_jogador', on_click=jogar )   

def main(page: ft.Page):     
    # Cria uma linha para exibir os botões lado a lado
    linha = ft.Row(
        controls=[
            pedra_maquina, 
            papel_maquina, 
            tesoura_maquina
            ],  # Adiciona instâncias do MeuConteiner
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        spacing=20
        
    )
    
    # Cria um container para a linha de botões
    container_maquina = ft.Container(
        content=linha,
        padding=20,
        border_radius=10,
        bgcolor="lightblue",
        height=150,
        alignment=ft.alignment.center
    )
    page.add(container_maquina)
    
    # Cria um container adicional para a área de jogo
    area_jogo = ft.Container(
        content=ft.Text("Área do Jogo", size=20, color=ft.colors.WHITE),  # Adiciona um texto de exemplo
        bgcolor="red",
        height=300,
        alignment=ft.alignment.center
    )
    page.add(area_jogo)    
    
    # Cria um container para o usuario
    container_jogador = ft.Container(
        content=ft.Row(
            controls=[
                pedra_player,
                papel_player,
                tesoura_player      
                ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            spacing=20            
            ),
        padding=20,
        border_radius=10,
        bgcolor="lightblue",
        height=150,
        alignment=ft.alignment.center
    )
    
    page.add(container_jogador)

if __name__ == "__main__":
    ft.app(target=main)
