frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso+= junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase noa é um palindromo.')