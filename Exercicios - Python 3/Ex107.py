from utilidadescevEx111 import moeda

p = float(input('Digite o preço: R$ '))
taxa = int(input('Digite a taxa para aumentar: '))
taxa2 = int(input('Digite a taxa para reduzir: '))
print(f'A matede {p} é {moeda.metade(p)} ')
print(f'O dobro de {p} é {moeda.dobro(p)} ')
print(f'Aumentando 10%, temos {moeda.aumentar(p, taxa)} ')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, taxa2)} ')
