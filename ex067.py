while True:
    print('-='*16)
    n = int(input('Quer vê a tabuada de qual valor? '))
    print('-='*16)
    if n <= -1:
        break
    else:
        for c in range(1, 11):
            multi = c * n
            print(f'{c} x {n} = {multi}')
print('Programa Tabuada Encerrado. Volte sempre!')