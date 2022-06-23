num = 0
soma = 0
cont = 0
num = int(input('Digite um numero [999 para acabar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para acabar]: '))
print('Você digitou {} numero e a soma entre eles foi {}.'.format(cont, soma))
