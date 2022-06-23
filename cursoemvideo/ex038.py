v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
if v2 > v1:
    print('O segundo valor é maior.')
elif v1 == v2:
    print('Não existe valor maior, os dois são iguais.')
elif v1 > v2:
    print('O primeiro valor é o maior.')
