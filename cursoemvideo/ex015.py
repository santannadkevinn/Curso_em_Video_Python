d = float(input('Quantos dias aludados? '))
k = float(input('Quantos KM rodados? '))
pk = 0.15 * k
pd = d * 60
print('Total a pagar é de R${}'.format(pk + pd))