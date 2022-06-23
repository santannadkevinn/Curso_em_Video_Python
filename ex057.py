sexo = str(input('Digite seu sexo: [M/S] ')).strip()[0].upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip()[0].upper()
print('Sexo {} registrado com sucesso'.format(sexo))