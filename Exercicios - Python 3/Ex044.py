print('{:=^40} '.format(' Lojas Max '))
preco = float(input('Digite o preço normal do produto: R$ '))
print('''Condição de pagamento:
[ 1 ]\033[1;32mDinheiro ou cheque:\033[m 10% de desconto
[ 2 ]\033[1;34mCartão:\033[m 5% de desconto
[ 3 ]\033[1;34mCartão 2x:\033[m preço normal
[ 4 ]\033[1;34mCartão 3x ou mais:\033[m 20% de \033[31mjuros\033[m''')
escolha = int(input('Escolha alguma das opções acima: '))
if escolha == 1:
    print('Pagando com dinheiro ou cheque o produto de R${} vai para R${:.2f} com 10% de desconto '.format(preco, preco - (preco * 10 /100)))
elif escolha == 2:
    print('Pagando com o cartão o produto de R${} vai para R${:.2f} com 5% de desconto '.format(preco, preco - (preco * 5 / 100)))
elif escolha == 3:
    print('Você ira pagar R${} '.format(preco))
elif escolha == 4:
    print('Parcelando em 3x ou mais o produto de R${} vai para R${:.2f} com 20% de juros '.format(preco, preco + (preco * 20 / 100)))
else:
    print('Escolha uma opção valida! ')

