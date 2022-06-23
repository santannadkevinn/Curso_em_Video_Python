r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r2 == r3:
    print('Parabéns, você consiguiu montar um triangulo EQUILÁTERO.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 != r3 and r2 == r3 != r1:
    print('Parabéns, você conseguiu montar um triangulo ISÓCELES')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 != r3:
    print('Parabéns, você conseguiu montar um triangulo ESCALENO.')
else:
    print('Seu idiota, você não sabe nem criar um triangulo?')