from random import randint
win = 0
print('-='*16)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*16)
while True:
    valor = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    computer = randint(0, 10)
    soma = computer + valor
    resto = soma % 2
    if resto == 0:
        if pi == 'P':
            win += 1
            print('Você ganhou!')
            print(f'Você jogou {valor} e o computador jogou {computer}. Total de {soma}. Deu PAR!')
        elif pi == 'I':
            break
    if resto == 1:
        if pi == 'P':
            break
        elif pi == 'I':
            win += 1
            print('Você ganhou!')
            print(f'Você jogou {valor} e o computador jogou {computer}. Total de {soma}. Deu ÍMPAR!')
print('Você perdeu!')
print('-='*16)
print(f'GAME OVER! Você venceu {win} vezes. ')
