print('Digite a distância da sua viagem para saber o preço de sua passagem.')
distancia = float(input('Distância da sua viagem: '))
print('-'*87)
if distancia <= 200:
    n1= int(distancia)
    n2 = n1 * 0.50
    print('Uma viagem de {}Km é menor que 200Km, portanto o preço da passagem sera R$0.50 por Km.\nO preço da passagem sera R${:.2f} '.format(n1, n2))
else:
    n1= int(distancia)
    n2= n1 * 0.45
    print('Uma viagem de {}Km é maior que 200Km, portanto o preço da passagem sera R$0.45 por Km.\nO preço da passsagem sera R${:.2f} '.format(n1, n2))
print('Tenha um bom dia!')
print('-'*87)

#ou
# n2 = distancia * 0.50 if distancia <= 200 else distancia * 0.45 | funciona assim tambem