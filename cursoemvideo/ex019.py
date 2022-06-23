import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o numero do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
p = [a1, a2, a3, a4]
print(f'O aluno que vai limpar o quadro é {random.choice(p)}')
