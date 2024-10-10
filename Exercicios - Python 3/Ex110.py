from utilidadescevEx111 import moeda


#Foi criado o def resumo():

p = float(input('Digite o preço: R$ '))
taxa = int(input('Digite a taxa para aumentar (%): '))
taxa2 = int(input('Digite a taxa para reduzir (%): '))
moeda.resumo(p, taxa, taxa2)