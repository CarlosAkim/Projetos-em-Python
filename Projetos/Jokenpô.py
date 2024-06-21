from random import choice
jogador_vitoria = 0
maquina_vitoria = 0
jogador_funcao = 0
maquina_funcao = 0

def jogador():
    esc_jogador = input('Escolha entre Pedra, Papel ou Tesoura: ')
    esc_jogador = esc_jogador.lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('Valor escolhido está errado...')
        jogador()


def maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


def jogo():
    jogador_vitoria = 0
    maquina_vitoria = 0
    for x in range(3):
        esc_jogador = jogador()
        esc_maquina = maquina()
        if esc_jogador == 'tesoura':
            if esc_maquina == 'tesoura':
                print('Deu empate')

            elif esc_maquina == 'papel':
                print('Jogador venceu')
                jogador_vitoria += 1

            elif esc_maquina == 'pedra':
                print('Maquina venceu')
                maquina_vitoria += 1

        elif esc_jogador == 'pedra':
            if esc_maquina == 'tesoura':
                print('Jogador venceu')
                jogador_vitoria += 1

            elif esc_maquina == 'papel':
                print('Maquina venceu')
                maquina_vitoria += 1

            elif esc_maquina == 'pedra':
                print('Deu empate')

        elif esc_jogador == 'papel':
            if esc_maquina == 'tesoura':
                print('Maquina venceu')
                maquina_vitoria += 1

            elif esc_maquina == 'papel':
                print('Deu empate')

            elif esc_maquina == 'pedra':
                print('Jogador venceu')
                jogador_vitoria += 1

    return jogador_vitoria, maquina_vitoria


print('Vamos começar a jogar!')

[jogador_funcao,maquina_funcao] = jogo()

while True:
    jogador_vitoria += jogador_funcao
    maquina_vitoria += maquina_funcao
    esc_jogador = input('Quer continue jogando? ')

    if esc_jogador in ['SIM', 'Sim', 's', 'sim', 'SiM', 'ss', 'Ss']:
        [jogador_funcao,maquina_funcao] = jogo()

    elif esc_jogador in ['NAO', 'Nao', 'n', 'nao', 'não', 'nn']:
        print(
            f'A maquina venceu {maquina_vitoria} vezes, O jogador venceu {jogador_vitoria} vezes!')
        break
    else:
        print('Valor digitado não está na opção  de (s/n), vamos tentar novamente')
