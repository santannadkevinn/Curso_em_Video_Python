from random import randint
from time import sleep
gamer = int(input('''Faça sua escolha perdedor.
[0] Pedra
[1] Papel
[2] Tesoura
Sua escolha é: '''))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolhido = randint(0, 2)
print('\033[7;30;45mJO\033[m')
sleep(1)
print('\033[7;31;40mKEN\033[m')
sleep(1)
print('\033[0;30;44mPO\033[m')
print('\033[0;32m=-\033[m'*20)
print('Computador jogou \033[0;31m{}\033[m'.format(lista[escolhido]))
print('Jogador jogou \033[0;36m{}\033[m'.format(lista[gamer]))
print('\033[0;32m-=\033[m'*20)
if escolhido == 0: #computador escolher pedra
    if gamer == 0:
        print('Empate')
    elif gamer == 1:
        print('Jogador vence.')
    elif gamer == 2:
        print('Computador vence')
    else:
        print('Jogada invalida')
elif escolhido == 1:
    if gamer == 0:
        print('Jogador vence')
    elif gamer == 1:
        print('Empate')
    elif gamer == 2:
        print('Computador vence')
    else:
        print('Jogada invalida')
elif escolhido == 2:
    if gamer == 0:
        print('Computador vence')
    elif gamer == 1:
        print('Jogador vence')
    elif gamer == 2:
        print('Empate')
    else:
        print('Jogada invalida')
