media = 0
soma = 0
maioridadehomem = 0
nomevelhor = ''
mulheridade = 0
for c in range(1, 5):
    print('-='*5, '{}° Pessoa'.format(c), '=-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelhor = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelhor =  nome
    if sexo in 'Ff' and idade < 20:
        mulheridade += 1
mediaidade = soma / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velhor tem {} anos e seu nome é {}.'.format(maioridadehomem, nomevelhor))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheridade))
