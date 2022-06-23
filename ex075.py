num = (int(input('Primeiro valor: ')),
       int(input('Primeiro valor: ')),
       int(input('Primeiro valor: ')),
       int(input('Primeiro valor: ')), )
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'A posição do primeiro numero 3 é {num.index(3)+1}°')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')