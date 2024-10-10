valores = list()
for c in range(1, 5+1):
    valores.append(int(input(f'Digite o {c}º valor: ')))
print('=-='*15)
print(f'Você digitou os valores {valores} ')
print(f'O maior valor é o {max(valores)} na posição {valores.index(max(valores))+1} ')
print(f'O menor valor é o {min(valores)} na posição {valores.index(min(valores))+1} ')
print('=-='*15)
