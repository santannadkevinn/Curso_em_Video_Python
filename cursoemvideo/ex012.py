p = float(input('Valor original:'))
d = float(input('Desconto para o produto:'))
de = d / 100
print('Valor original: {}'.format(p))
print('Você ganhou R${} de desconto'.format(p * 0.05))
print('Valor final é de R${:.2}.'.format(p - p *0.05))
