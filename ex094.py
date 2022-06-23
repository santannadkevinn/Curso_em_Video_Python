from time import process_time
people = {}
galera = list()
soma = count = media = 0
pessoal = []
women = []
while True:
    gente = people['nome'] = str(input('Nome: '))
    sex = people['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    adc = people['idade'] = int(input('Idade: '))
    pessoal.append(people)
    count += 1
    soma += adc
    media = soma / count
    galera.append(people.copy)
    if sex in 'Ff':
        women.append(str(gente))
    q = str(input('Quer continuar? [S/N] '))
    if q in 'Nn':
        break
print(f'O grupo tem {count} pessoas.')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: {", ".join(women)}')
for p in people:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< Encerrado >>')