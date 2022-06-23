from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} de idade e esta na categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos de idade e esta na categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos de idade e sua categoria é JUNIOR.'.format(idade))
elif idade == 19:
    print('Você tem {} anos de idade e sua categoria é SÊNIOR.'.format(idade))
elif idade > 20:
    print('Você tem {} de idade e sua categoria é MASTER.'.format(idade))