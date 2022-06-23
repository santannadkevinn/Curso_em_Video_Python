progressao = 1
termo = int(input('Primeiro termo: '))
razao = int(input(('Razão: ')))
decimo = termo + (10 - 1) * razao
ter = termo
cont = 1
while cont <= 10:
    print('{} ->'.format(ter), end= '')
    ter += razao
    cont += 1
print('Fim')