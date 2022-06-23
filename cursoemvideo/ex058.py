from random import choice
num = 0
count = 0
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = choice(list)
while computador != num:
    computador = choice(list)
    num = int(input('Digite um numero de 0 à 10: '))
    count += 1
    if num != computador and num <= 10:
        print('A resposta foi {} idiota, tente de novo.'.format(computador))
    if computador == num:
        print('Parabéns! Você acertou')
        print('Você precisou de {} tentativas para vencer'.format(count))
    if num > 10:
        print('Você tem demencia? É de 0 à 10')
        print('Tente de novo!')
