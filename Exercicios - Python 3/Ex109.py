from utilidadescevEx111 import moeda

p = float(input('Digite o preço: R$ '))
taxa = int(input('Digite a taxa para aumentar (%): '))
taxa2 = int(input('Digite a taxa para reduzir (%): '))
print('-'*50)
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)} ')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)} ')
print(f'Aumentando 10%, temos {moeda.aumentar(p, taxa, True)} ')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, taxa2, True)} ')
print('-'*50)