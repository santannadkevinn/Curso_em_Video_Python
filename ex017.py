'''co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjecente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjecente: '))
hi = hypot(co,ca)
print('A hypotenusa vai medir {}'.format(hi))

