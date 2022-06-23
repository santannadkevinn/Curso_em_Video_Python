n = int(input('Digite um numero para calcular o fatorial: '))
f = 1
print('Calculando {}!'.format(n), end= '')
for b in range(n, 0, -1):
    print('{}'.format(b),end= '')
    print('x' if n > 1 else '=', end= '')
    f *= n
    n -= 1
print('{}'.format(f))