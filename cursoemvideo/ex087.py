matriz = [[], [], []]
pares = maior = scol =  0
for posicao, valores in enumerate(matriz):
    for c in range(0,3):
        valor = matriz[posicao].append(int(input(f'Digite um valor para [{posicao}, {c}]: ')))
for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]', end='')
            if matriz[l][c] % 2 == 0:
                pares += matriz[l][c]
        print()
print(f'A soma dos valores pares é {pares}')
for l in range(0, 3):
    scol += matriz[l][c]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1] [c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')