matriz = [[], [], []]
for posicao, valores in enumerate(matriz):
    for c in range(0,3):
        matriz[posicao].append(int(input(f'Digite um valor para [{posicao}, {c}]: ')))
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()