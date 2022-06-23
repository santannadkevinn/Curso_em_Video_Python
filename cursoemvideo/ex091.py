from random import randint
from time import sleep
jogadores = {}
for c in range(1, 5):
    valor = jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'O jogador{c} tirou {valor}')
    sleep(1)
print('=-'*20)
print('Ranking dos Jogadores:')
count = 1
while count < 5:
    for k in sorted(jogadores, key=lambda key:jogadores[key], reverse=True):
        print(f'{count}° lugar: {k} com {jogadores[k]} ')
        count += 1
        sleep(1)
