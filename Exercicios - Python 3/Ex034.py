salario = int(input('Digite o seu salário: '))
if salario < 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O seu salário agora é R${:.0f} '.format(novo))
