ni = int(input('Digite um numero inteiro qualquer:'))
con = int(input('Escolha o tipo de converção:\n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n Qual sua escolha?  '))
if con == 1:
    print('O numero {} corresponde a {} em binário.'.format(ni, bin(ni)[2:]))
elif con == 2:
    print('O numero {} corresponde a {} em octal.'.format(ni, oct(ni)[2:]))
elif con == 3:
    print('O numero {} corresponde a {} em hexadecimal.'.format(ni, hex(ni)[2:]))