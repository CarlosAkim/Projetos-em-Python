import flet as ft #type:ignore
import random
import threading
from time import sleep

# Classe personalizada que representa um container com uma imagem e comportamento de clique
class MeuConteiner(ft.Container):
    def __init__(self, image_url, id, on_click=None):
        # Inicializa o Container com as propriedades básicas
        super().__init__()
        self.on_click = on_click  # Função a ser chamada quando o container for clicado
        self.height = 80  # Altura do container
        self.width = 100  # Largura do container
        self.border_radius = 15  # Borda arredondada do container
        self.alignment = ft.alignment.center  # Alinhamento do conteúdo do container
        self.content = ft.Image(src=image_url)  # Imagem a ser exibida no container
        self._opacity = 1.0  # Opacidade inicial do container (totalmente visível)
        self.id = id  # ID do container, usado para identificar o elemento
        if on_click:
            # Se a função de clique for fornecida, associa-a ao evento de clique
            self.on_click = lambda e: on_click(id)
            
        # Propriedade para obter a opacidade do container
        @property    
        def opacity(self) -> float:
            return self._opacity
        
        # Propriedade para definir a opacidade do container
        @opacity.setter
        def opacity(self, porcentagem: float):
            self._opacity = porcentagem

# Função principal do aplicativo Flet
def main(page: ft.Page):
    # Variável global para armazenar a escolha da máquina
    global escolha_maquina

    # Função que controla a opacidade dos containers da máquina e retorna a escolha da máquina
    def jogar_maquina() -> str:
        global escolha_maquina
        jg = random.randint(1, 3)  # Escolha aleatória entre 1, 2 e 3 (pedra, papel, tesoura)
                
        # Define a escolha da máquina com base no valor aleatório
        if jg == 1:
            pedra_maquina.opacity = 1.0
            papel_maquina.opacity = 0.3
            tesoura_maquina.opacity = 0.3
            escolha_maquina = 'pedra'
        elif jg == 2:
            papel_maquina.opacity = 1.0
            pedra_maquina.opacity = 0.3
            tesoura_maquina.opacity = 0.3
            escolha_maquina = 'papel'
        else:
            tesoura_maquina.opacity = 1.0
            pedra_maquina.opacity = 0.3
            papel_maquina.opacity = 0.3
            escolha_maquina = 'tesoura'
        
        page.update()  # Atualiza a página para refletir as mudanças de opacidade
    
    # Função que controla a jogada do jogador e aciona a jogada da máquina
    def jogar(container_id):
        jogada_player = None  # Inicializa a variável que armazena a jogada do jogador
        
        # Define a jogada do jogador com base no container clicado
        if container_id == 'pedra_jogador':
            pedra_player.opacity = 1.0
            papel_player.opacity = 0.3
            tesoura_player.opacity = 0.3
            jogada_player = 'pedra'
        elif container_id == 'papel_jogador':
            papel_player.opacity = 1.0
            pedra_player.opacity = 0.3
            tesoura_player.opacity = 0.3
            jogada_player = 'papel'
        elif container_id == 'tesoura_jogador':
            tesoura_player.opacity = 1.0
            pedra_player.opacity = 0.3
            papel_player.opacity = 0.3
            jogada_player = 'tesoura'
        
        page.update()  # Atualiza a página para refletir as mudanças de opacidade
        
        # Iniciar a jogada da máquina em paralelo usando uma thread
        jg_maquina = threading.Thread(target=jogar_maquina)
        jg_maquina.start()  # Inicia a thread da jogada da máquina
        jg_maquina.join()  # Espera a thread terminar antes de continuar
        
        # Iniciar a comparação das jogadas em uma nova thread
        threading.Thread(target=comparar_jogadas, args=(jogada_player, escolha_maquina)).start()

    # Função que compara as jogadas do jogador e da máquina e determina o vencedor
    def comparar_jogadas(jogada_player, jogada_maquina):
        sleep(0.2)  # Pequena pausa para garantir que a jogada da máquina foi concluída
            
        # Verifica se houve um empate
        if jogada_player == jogada_maquina:
            mostrar_resultado('Empate')
        # Verifica se o jogador ganhou
        elif ((jogada_player == 'pedra' and jogada_maquina == 'tesoura') or 
              (jogada_player == 'papel' and jogada_maquina == 'pedra') or
              (jogada_player == 'tesoura' and jogada_maquina == 'papel')):
            mostrar_resultado("Você Ganhou!!")
        # Caso contrário, a máquina ganhou
        else:
            mostrar_resultado("Máquina Ganhou!")
        
    
    # Função que exibe o resultado do jogo na interface
    def mostrar_resultado(text: str):
        resultado_text.value = text  # Define o texto do resultado
        page.update()  # Atualiza a página para refletir o resultado
    
    # Imagens usadas no jogo
    pedra_img = "Projetos-em-Python\Projetos\Jokenpo_flet\imagems jokepo\pedra.png"
    papel_img = "Projetos-em-Python\Projetos\Jokenpo_flet\imagems jokepo\papel.png"
    tesoura_img = "Projetos-em-Python\Projetos\Jokenpo_flet\imagems jokepo\Tesoura.png"

    # Cria instâncias do MeuConteiner com imagens para a máquina
    pedra_maquina = MeuConteiner(image_url=pedra_img, id="pedra_maquina")
    papel_maquina = MeuConteiner(image_url=papel_img, id="papel_maquina")
    tesoura_maquina = MeuConteiner(image_url=tesoura_img, id='tesoura_maquina')

    # Cria instâncias do MeuConteiner com imagens para o jogador, com comportamento de clique
    pedra_player = MeuConteiner(image_url=pedra_img, id='pedra_jogador', on_click=jogar)
    papel_player = MeuConteiner(image_url=papel_img, id='papel_jogador', on_click=jogar)
    tesoura_player = MeuConteiner(image_url=tesoura_img, id='tesoura_jogador', on_click=jogar)
    
    # Cria uma linha (Row) para exibir os botões da máquina lado a lado
    linha = ft.Row(
        controls=[
            pedra_maquina, 
            papel_maquina, 
            tesoura_maquina
        ],  # Adiciona instâncias do MeuConteiner
        alignment=ft.MainAxisAlignment.SPACE_AROUND,  # Alinhamento dos botões
        spacing=20  # Espaçamento entre os botões
    )
    
    # Cria um container para a linha de botões da máquina
    container_maquina = ft.Container(
        content=linha,
        padding=20,  # Padding do container
        border_radius=10,  # Borda arredondada do container
        bgcolor="lightblue",  # Cor de fundo do container
        height=150,  # Altura do container
        alignment=ft.alignment.center  # Alinhamento do conteúdo do container
    )
    page.add(container_maquina)  # Adiciona o container da máquina à página
    
    resultado_text = ft.Text("Área do Jogo", size=20, color=ft.colors.WHITE)  # Texto para exibir o resultado
    # Cria um container adicional para a área de jogo
    area_jogo = ft.Container(
        content=resultado_text,  # Adiciona o texto de resultado ao container
        bgcolor="red",  # Cor de fundo da área de jogo
        height=300,  # Altura da área de jogo
        alignment=ft.alignment.center  # Alinhamento do conteúdo na área de jogo
    )
    page.add(area_jogo)  # Adiciona a área de jogo à página
    
    # Cria um container para os botões do jogador
    container_jogador = ft.Container(
        content=ft.Row(
            controls=[
                pedra_player,
                papel_player,
                tesoura_player
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,  # Alinhamento dos botões do jogador
            spacing=20  # Espaçamento entre os botões do jogador
        ),
        padding=20,  # Padding do container do jogador
        border_radius=10,  # Borda arredondada do container do jogador
        bgcolor="lightblue",  # Cor de fundo do container do jogador
        height=150,  # Altura do container do jogador
        alignment=ft.alignment.center  # Alinhamento do conteúdo do container do jogador
    )
    
    page.add(container_jogador)  # Adiciona o container do jogador à página
    page.update()  # Atualiza a página para refletir todas as mudanças

# Ponto de entrada do aplicativo
if __name__ == "__main__":
    ft.app(target=main)  # Inicia o aplicativo Flet chamando a função main
