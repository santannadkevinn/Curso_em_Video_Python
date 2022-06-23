posicao_maior = []
posicao_menor = []
lista = []
for c in range(1,6):
    n = int(input(f'Digite o valor N° {c} :'))
    lista.append(n)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições {posicao_maior} ')
print(f'O menor valor digitado foi {min(lista)} nas posições {posicao_menor}')