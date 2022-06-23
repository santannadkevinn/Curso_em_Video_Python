from random import randint
from time import sleep
print('--'*20)
titulo = 'JOGA NA MEGA SENA'
print(titulo.center(35))
print('--'*20)
sorte = int(input('Quantos jogos você quer que eu sorteie? '))
numeros = []
for c in range(0, sorte):
    num = numeros.append([randint(1,61), randint(1,61),
           randint(1,61), randint(1,61),
           randint(1,61), randint(1,61)])
for posicao, v in enumerate(numeros):
    print(f'Jogo {posicao + 1}: {str(numeros[posicao])}')
    sleep(1)
