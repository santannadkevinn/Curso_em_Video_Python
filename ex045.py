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
if gamer == escolhido:
    print('Deu sorte. Empatamos.')
#pedra e tesoura
elif escolhido == 0 and gamer == 2:
    print('Otario! Eu ganhei.')
# tesoura e papel
elif escolhido == 2 and gamer == 1:
    print('Otario! Eu ganhei.')
# papel e pedra
elif escolhido == 1 and gamer == 0:
    print('Otario! Eu ganhei.')
elif escolhido == 2 and gamer == 0:
    print('Otario! Eu ganhei.')
else:
   print('Você é idiota. Escolha a opção correta.')
