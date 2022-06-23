from datetime import date
from time import sleep
pessoa = {}
while True:
    nome = pessoa['nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    pessoa['idade'] = date.today().year - ano
    ctps = int(input('Carteira de Trabalho (0 não tem): '))
    if ctps == 0:
        print('-='*20)
        print(f'Nome tem o valor {nome}')
        sleep(0.5)
        print(f'Idade tem o valor {date.today().year - ano}')
        sleep(0.5)
        print(f'Ctps tem o valor {ctps}')
        exit()
    else:
        pessoa['ctps'] = ctps
    contra = pessoa['contratação'] = int(input('Ano de Contratação: '))
    salario = pessoa['salario'] = float(input('Salário: R$ '))
    aposentadoria = pessoa['aposentadoria'] = contra + 35
    print('-='*20)
    print(f'Nome tem o valor {pessoa["nome"]}')
    sleep(0.5)
    print(f'idade tem o valor {pessoa["idade"]}')
    sleep(0.5)
    print(f'Ctps tem o valor {pessoa["ctps"]}')
    sleep(0.5)
    print(f'Contratação tem o valor {pessoa["contratação"]}')
    sleep(0.5)
    print(f'Salário tem o valor {pessoa["salario"]}')
    sleep(0.5)
    print(f'Aposentadoria tem o valor {pessoa["aposentadoria"]}')
    sleep(0.5)
    p = str(input(('Deseja continuar? [S/N] ')))
    if p in 'Nn':
        break
    else:
        pessoa.clear()
