from time import sleep
lista = [1, 2, 3, 4, 5]
p = 1
while p != lista:
    first = int(input('Digite o 1° valor: '))
    secund = int(input('Digite o 2° valor: '))
    menu = print('''[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5] SAIR DO PROGRAMA''')
    escolha = int(input('Qual a sua escolha: '))
    while escolha == 1:
        if escolha == 1:
            print('A soma de {} + {} = {}'.format(first, secund, first + secund))
            break
    while escolha == 2:
        if escolha == 2:
            print('A multiplicação de {} x {} = {}'.format(first, secund, first * secund))
            break
    while escolha == 3:
        if escolha == 3:
            if first < secund:
                print('O valor {} é maior que o valor {}.'.format(secund, first))
            else:
                print('O valor {} é maior que o valor {}.'.format(first, secund))
            break
    while escolha == 4:
        if escolha == 4:
            break
    while escolha == 5:
        print('Encerrando programa.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print('Encerrado')
        exit()
    while escolha > 5:
        escolha = int(input('Opção invalida! Tente novamente:'))
        break
