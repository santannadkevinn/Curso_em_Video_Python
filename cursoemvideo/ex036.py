valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto você ganha por mês? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= 300:
    print('\033[0;36;40mParabêns!!!\033[m Seu emprestimo foi aprovado.')
    print('O valor mensal do seu emprestimo é de {:.2f}'.format(prestacao))
elif prestacao > minimo:
    print('Infelizmente seu emprestimo foi recusado.')