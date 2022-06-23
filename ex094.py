soma = count = media = 0
pessoal = []
women = []
while True:
    people = {}
    gente = people['nome'] = str(input('Nome: '))
    sex = people['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    adc = people['idade'] = int(input('Idade: '))
    pessoal.append(people)
    count += 1
    soma += adc
    media = soma / count
    if sex in 'Ff':
        women.append(str(gente))
    q = str(input('Quer continuar? [S/N] '))
    if q in 'Nn':
        break
print(pessoal)
print(f'O grupo tem {count} pessoas.')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: {", ".join(women)}')
if pessoal["idade"] > media:
    print()