from datetime import date
ano = int(input('Digite um ano ou coloque 0 para colocar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))