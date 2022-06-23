from datetime import date
count = 0
soma = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu?  '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        count += 1
    else:
        soma += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE tambem tivemos {} pessoas menores de idade.'.format(count, soma))
