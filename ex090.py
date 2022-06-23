aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["nota"]}')
if aluno["nota"] > 7:
    print('Situação é igual a Aprovado.')
elif aluno["nota"] > 5:
    print('situação igua a Recuperação')
else:
    print('Situação é igual a Reprovado') 
    