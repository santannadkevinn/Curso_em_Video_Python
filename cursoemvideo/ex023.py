nun = int(input('Digite um numero de 0 à 9999: '))
u = nun // 1 % 10
d = nun // 10 %10
c = nun // 100 % 10
m = nun // 1000 % 10
print('Analizando o numero {}'.format(nun))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
