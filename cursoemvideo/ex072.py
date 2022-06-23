n = 'Zero', 'Um', 'Dois', 'Três', 'Quatro',\
    'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',\
    'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze',\
    'Quinze', 'Dezersei', 'Dezersete',\
    'Dezoito', 'Dezenove', 'Vinte'
while True:
    r = int(input('Digite um numero entre 0 e 20: '))
    while r > 20:
        r = int(input('Tente novamente! Digite um numero entre 0 e 20: '))
    while r < 0:
        r = int(input('Tente novamente! Digite um numero entre 0 e 20: '))
    print(f' Você digitou o numero {n[r]}')
    break
