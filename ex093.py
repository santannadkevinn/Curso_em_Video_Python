jodador = {}
gols = []
soma = 0
while True:
    while True:
        nome = jodador['jogador'] = str(input('Nome do jogador: '))
        quantidade = int(input(f'Quantas partidas {nome} jogou? '))
        for c in range(1, quantidade + 1):
            cont = int(input(f'Quantos gols na partida {c}: '))
            gols.append(cont)
            soma += cont
        jodador['gols'] = gols
        jodador['total'] = soma
        break
    print('=-'*30)
    print(jodador)
    print('=-'*30)
    print()
    print('=-'*30)
    print(f'O campo nome tem o valor {jodador["jogador"]}.')
    print(f'O campo gols tem o valor {jodador["gols"]}.')
    print(f'O campo total tem o valor {jodador["total"]}')
    print('=-'*30)
    print()
    print('=-'*30)
    print(f'O jogador {jodador["jogador"]} jogou {quantidade} partidas.')
    conta = 1
    while conta < quantidade:
            for v in jodador["gols"]:
                print(f'=> Na partida {conta}, fez {v} gols.')
                conta += 1
            print(f'Foi um total de {jodador["total"]} gols.')
    q = str(input('Quer continuar? [S/N] '))
    if q in 'Nn':
        exit()
    else:
        jodador.clear()