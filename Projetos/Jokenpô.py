"""
Este módulo fornece funcionalidades para um jogo de Pedra, Papel e Tesoura.
"""

from random import choice

jogador_vitoria = 0
maquina_vitoria = 0
jogador_funcao = 0
maquina_funcao = 0


def jogador() -> str:
    """
    Função para obter a escolha do jogador em um jogo de Pedra, Papel e Tesoura.

    A função solicita ao usuário que escolha entre "pedra", "papel" ou "tesoura", 
    converte a escolha para letras minúsculas e verifica se é válida. 
    Se a escolha for válida, ela é retornada; caso contrário, a função 
    solicita ao usuário que escolha novamente até que uma escolha válida seja feita.

    Retorna:
        str: A escolha do jogador, que pode ser "pedra", "papel" ou "tesoura".
    """

    # escolha do usuario
    esc_jogador: str = input('Escolha entre Pedra, Papel ou Tesoura: ')

    # convertendo a escolha do usuário para letras minúsculas
    esc_jogador = esc_jogador.lower()

    if esc_jogador in ['pedra', 'papel', 'tesoura']:
        return esc_jogador
    else:
        # caso o usuario escolha alguma opção que não exista
        print('Valor escolhido está errado...')
        return jogador()


def maquina() -> str:
    """
    Função para gerar uma escolha aleatória para a máquina em um jogo de Pedra, Papel e Tesoura.

    A função utiliza o módulo random para escolher aleatoriamente entre "pedra", "papel" e "tesoura", 
    retornando a escolha como uma string.

    Retorna:
        str: A escolha da máquina, que pode ser "pedra", "papel" ou "tesoura".
    """
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


def jogo() -> tuple:
    """
    Função para realizar um jogo de Pedra, Papel e Tesoura entre o jogador e a máquina.

    A função realiza três rodadas do jogo, onde o jogador escolhe entre "pedra", "papel" e "tesoura",
    e a máquina faz uma escolha aleatória. Os resultados de cada rodada são contabilizados para
    determinar o número de vitórias de cada um.

    Retorna:
        tuple: Uma tupla contendo duas variáveis inteiras:
            - jogador_vitoria: número de vitórias do jogador.
            - maquina_vitoria: número de vitórias da máquina.
    """
    jogador_vitoria = 0
    maquina_vitoria = 0

    resultado = {
        "tesoura": {
            "tesoura": "empate",
            "papel": "jogador venceu",
            "pedra": "maquina venceu"
        },
        "papel": {
            "tesoura": "maquina venceu",
            "papel": "empate",
            "pedra": "jogador venceu"
        },
        "pedra": {
            "tesoura": "jogador venceu",
            "papel": "maquina venceu",
            "pedra": "empate"
        }
    }
    for x in range(3):
        # escolha do usuario
        esc_jogador: str = jogador()

        # escolha da maquina
        esc_maquina: str = maquina()

        jogada = resultado[esc_jogador][esc_maquina]

        if jogada == "jogador venceu":
            print("Usuario venceu a Rodada")
            jogador_vitoria += 1

        elif jogada == "maquina venceu":
            print("Maquina venceu a rodada")
            maquina_vitoria += 1

        else:
            print("Empate")

    # retorna uma tupla com os resultados
    return jogador_vitoria, maquina_vitoria


print('Vamos começar a jogar!')

# passamos a variavel para receber o resultado do jogo
[jogador_funcao, maquina_funcao] = jogo()

# Loop principal do jogo
while True:
    # Adiciona os resultados das funções jogador_funcao e maquina_funcao às vitórias do jogador e da máquina
    jogador_vitoria += jogador_funcao
    maquina_vitoria += maquina_funcao

    # Pergunta ao jogador se ele deseja continuar jogando
    esc_jogador = input('Quer continuar jogando? ')

    # Verifica se o jogador deseja continuar jogando
    if esc_jogador in ['SIM', 'Sim', 's', 'sim', 'SiM', 'ss', 'Ss']:
        # Chama a função jogo e armazena os resultados em jogador_funcao e maquina_funcao
        [jogador_funcao, maquina_funcao] = jogo()

    # Verifica se o jogador deseja parar de jogar
    elif esc_jogador in ['NAO', 'Nao', 'n', 'nao', 'não', 'nn']:
        # Imprime o resultado final das vitórias do jogador e da máquina
        print(
            f'A máquina venceu {maquina_vitoria} vezes, o jogador venceu {jogador_vitoria} vezes!'
        )
        # Sai do loop
        break

    # Caso o valor digitado não seja uma opção válida
    else:
        # Informa ao jogador que a opção digitada é inválida e solicita nova entrada
        print(
            'Valor digitado não está na opção de (s/n), vamos tentar novamente'
        )
