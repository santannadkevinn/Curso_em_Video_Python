soma = count = 0
while True:
    n = int(input('Digite um valor [999 para parar] '))
    if n == 999:
        break
    soma = soma + n
    count += 1
print(f'A soma dos {count} valores foi {soma}')