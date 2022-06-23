termo = int(input('Primeiro termo: '))
razao = int(input(('Razão: ')))
decimo = termo + (10 - 1) * razao
ter = termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(ter), end='')
        ter += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Fim!')
