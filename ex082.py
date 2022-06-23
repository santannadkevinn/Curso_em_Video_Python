lista = []
lista_impa= []
lista_par = []
while True:
    i = int(input('Digite um numero: '))
    lista.append(i)
    if i % 2 == 0:
        lista_par.append(i)
    if i % 2 == 1:
        lista_impa.append(i)
    n = str(input('Quer continuar? [S/N] ')).strip().upper()
    if n == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impa}')