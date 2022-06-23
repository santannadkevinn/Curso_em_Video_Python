n = int(input('Digite um numero: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é par.'.format(n))
else:
    print('O numero {} é ímpar'.format(n))