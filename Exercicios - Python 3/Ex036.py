casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite os anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f} '.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo \033[0;32mconcedido\033[m!')
else:
    print('Emprestimo \033[0;31mnegado\033[m!')