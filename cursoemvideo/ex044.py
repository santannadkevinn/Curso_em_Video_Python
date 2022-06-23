valor = float(input('Digite o valor do produto: '))
pagamento = int(input('Escolha a forma de pagamento:\n 1 - À vista no dinheiro ou cheque: 10% Desconto\n 2 - À vista no cartão: 5% Desconto\n 3 - Até 2x no cartão: Preço normal\n 4 - 3x ou mais no cartão: 20% de juros.\n Qual sua escolha: '))
if pagamento == 1:
    print('Muito obrigado por comprar conosco.')
    print('Você escolheu a opção N°1. o valor final foi R${:.2f}'.format(valor - (valor / 100 * 10)))
elif pagamento == 2:
    print('Muito obrigado por comprar conosco.')
    print('Você escolheu a opção N°2. O valor final foi R${:.2f}'.format(valor - (valor / 100 * 5)))
elif pagamento == 3:
    print('Muito obrigado por comprar conosco.')
    print('Você escolheu a opção N°3. O valor final foi R${:.2f}'.format(valor))
elif pagamento == 4:
    print('Muito obrigado por comprar conosco.')
    print('Você escolheu a opção N°4. O valor final foi R${:.2f}'.format(valor + (valor / 100 * 20)))
else:
    print('Por favor, selecione uma das opções acima.')