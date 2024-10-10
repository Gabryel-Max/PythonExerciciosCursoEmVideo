pesoLista = []
for contagem in range(1, 4):
    peso = float(input('Insira o {}º peso: '.format(contagem)))
    pesoLista.append(peso)
print('O menor peso é: {}'.format(min(pesoLista)))  # Menor item da lista
print('O maior peso é: {}'.format(max(pesoLista)))  # Maior item da lista