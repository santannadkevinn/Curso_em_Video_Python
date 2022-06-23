aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["nota"]}')
if aluno["nota"] > 4.9:
    print('Situação é igual a Aprovado.')
else:
    print('Situação é igual a Reprovado')