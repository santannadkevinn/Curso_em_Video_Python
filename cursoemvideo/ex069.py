age = 0
m = 0
hi = 0
while True:
    print('-='*17)
    print('CADASTRE UMA PESSOA')
    print('-='*17)
    idade = int(input('Idade: '))
    sex = str(input('Sexo: ')).strip().upper()
    if idade < 20:
        if sex == 'F':
            m += 1
    if idade >= 18:
        age += 1
    while sex != 'M' and sex != 'F':
        sex = str(input('Digite novamente o sexo: [M/F]' )).strip().upper()
    if sex == 'M':
        hi += 1
    print('-='*17)
    restart = str(input('Deseja continuar? [S/N]')).strip().upper()
    print('-='*17)
    if restart == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {age}')
print(f'Ao todo temos {hi} homens cadastrados')
print(F'E temos {m} mulheres com menos de 20 anos')

