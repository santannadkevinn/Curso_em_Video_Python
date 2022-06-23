alunos = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Digite a 1° nota: '))
    n2 = float(input('Digite a 2° nota: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'{"N°.":<4}{"Nome":<10}{"Média":>5}')
print('-=' * 26)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>.1f}')
while True:
    stop = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if stop == 999:
        break
    else:
        print(f'As notas de {a[0]} são {a[1]}')
