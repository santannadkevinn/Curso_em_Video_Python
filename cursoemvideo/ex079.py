lista = []
while True:
    v = int(input('Digite uma valor: '))
    if v in lista:
        print('Valor duplicado! Não vou adcionar...')
    else:
        lista.append(v)
    cont = str(input('Quer continuar? [S/N]' )).strip().upper()
    if cont == 'N':
        break
lista.sort(lista)
print(lista)