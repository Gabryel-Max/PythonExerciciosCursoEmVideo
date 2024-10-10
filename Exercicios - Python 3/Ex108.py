from utilidadescevEx111 import moeda

p = float(input('Digite o preço: R$ '))
taxa = int(input('Digite a taxa para aumentar (%): '))
taxa2 = int(input('Digite a taxa para reduzir (%): '))
print('-'*50)
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))} ')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))} ')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, taxa))} ')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, taxa2))} ')
print('-'*50)