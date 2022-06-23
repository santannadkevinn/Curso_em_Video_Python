salario = float(input('Digite seu salário:'))
a = salario + (salario / 100 * 15)
b = salario + (salario / 100 * 10)
if salario <= 1250:
    print('Você teve um aumento de 15% e seu salario agora é R${:.2f}.'.format(a))
else:
    print('Você teve um aumento de 10% e seu salario agora é R${:.2f}.'.format(b))