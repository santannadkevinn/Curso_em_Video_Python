n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Infelismente sua nota foi {:.1f} e você foi reprovado.'.format(media))
elif 6.9 > media >= 5:
    print('Deu sorte malandro, você tirou {:.1f} e esta de recuperação.'.format(media))
elif media >= 7.0:
    print('Parabens, você tirou {:.1f} e foi aprovado.'.format(media))
