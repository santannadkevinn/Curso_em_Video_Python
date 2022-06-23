d = int(input('Digite a distancia: '))
if d <= 200:
    print('O valor da sua passagem é R${:.2f}'.format(d * 0.50))
else:
    print('O valor da sua passagem é R${:.2f}'.format(d * 0.45))