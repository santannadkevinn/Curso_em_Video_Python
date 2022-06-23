titulo = 'Banco KDS'
print('='*20)
print(titulo.center(20))
print('='*20)
saque = int(input('Qual o valor de saque: '))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    while saque >= 50:
        saque -= 50
        cont50 += 1
    while saque >= 20:
        saque -= 20
        cont20 += 1
    while saque >= 10:
        saque -= 10
        cont10 += 1
    while saque >= 1:
        saque -= 1
        cont1 += 1
    break
print(f'Total de {cont50} cédulas de R$50.00')
print(f'Total de {cont20} cédulas de R$20.00')
print(f'Total de {cont10} cédulas de R$10.00')
print(f'Total de {cont1} cédulas de R$1.00')