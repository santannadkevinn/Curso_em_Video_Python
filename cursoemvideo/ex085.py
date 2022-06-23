lista = [[], []]
count = 0
for c in range(1, 8):
    valores = int(input(f'Digite o {c}°: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')