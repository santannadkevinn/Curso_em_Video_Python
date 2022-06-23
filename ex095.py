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
    q = str(input('Quer continuar? [S/N] '))
    if q in 'Nn':
        break
print(jodador)
conta = 1
while conta < quantidade:
        for v in jodador["gols"]:
            print(f'=> Na partida {conta}, fez {v} gols.')
            conta += 1
        print(f'Foi um total de {jodador["total"]} gols.')
