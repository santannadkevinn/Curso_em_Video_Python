'''import math
n = float(input('Digite um numero real: '))
print('O numero real {} tem a parte inteira {}.'.format(n, math.floor(n)))'''

'''num = float(input('Digite um numero real: '))
print('O valor de digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''

from math import trunc
n = float(input('Digite um numero real: '))
print('O valor digitafo foi {} e sua porção inteira é {}'.format(n, trunc(n)))