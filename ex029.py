v = int(input('Digite a velocidade:'))
m = v - 80
if v <= 80:
    print('Tudo certo, pode continuar.')
else:
    print('Você estava {} acima da velocidade maxima e foi multado em R${:.2f}.'.format(m, m * 7))
