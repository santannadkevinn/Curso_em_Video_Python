total = menor = mais = maior = count = 0
prod = ''
print('=-' * 20)
print('''           LOJÃO DO 10
ONDE TUDO É ACIMA DE 10 REAIS''')
print('=-' * 20)
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: '))
    count += 1
    if preco >= 1000.00:
        mais += 1
    total += preco
    if count == 1 or preco < menor:
        menor = preco
        prod = nome
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'O valor total de compra foi R${total:.2f}')
print(f'Temos {mais} produtos que custa mais de R$1000.00')
print(f'O produto mais barato foi {prod} que custa {menor:.2f}')
