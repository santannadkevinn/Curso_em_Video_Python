count = 0
lista = []
while True:
    s = int(input('Digite um valor: '))
    lista.append(s)
    count += 1
    n = str(input('Quer continuar? [S/N] ')).upper().strip()
    if n == 'N':
        break
print(f'Você digitou {count} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')