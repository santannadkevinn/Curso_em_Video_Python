peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {:.1f} e você esta abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} e você esta no peso ideal.'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.1f} e você esta acima do peso'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {:.1f} e você esta obeso.'.format(imc))
elif imc > 40:
    print('Voce vai explodir filho de uma egua.')