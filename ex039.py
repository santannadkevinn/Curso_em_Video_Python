from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
da = date.today().year - ano
if da < 18:
    print('Você tem {} anos e faltam {} anos para vc se alistar.'.format(da, 18 - da))
    saldo = 18 - da
    anos = date.today().year + saldo
    print('Seu alistamento será em {}.'.format(anos))
elif da == 18:
    print('Voce tem {} anos e precisa comparecer ao centro de alistamento.'.format(da))
elif da > 18:
    saldo = da - 18
    print('Você tem {} e ja passou do tempo para o alistamento que foi {} anos atrás.'.format(da, da - 18))
    anos = date.today().year - saldo
    print('Seu alistamento foi em {}.'.format(anos))