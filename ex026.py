frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira letra apareceu na posição {}'.format(frase.find('A') + 1))
print('A ultima letra apareceu na posição {}'.format(frase.rfind('A') + 1))