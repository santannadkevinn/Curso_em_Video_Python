import math
an = float(input('Digite um ângulo: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, math.sin(math.radians(an))))
print('O ângulo de {} o COSSENO de {:.2f}'.format(an, math.cos(math.radians(an))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, math.tan(math.radians(an))))