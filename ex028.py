from random import choice
n = int(input('Digite um numero de 0 à 5: '))
nr = [0, 1, 2, 3, 4, 5]
r = choice(nr)
if n == r:
    print('Parabens, você acertou.')
else:
    print('A resposta foi {} idiota, tente de novo.'.format(r))