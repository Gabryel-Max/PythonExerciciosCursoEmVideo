from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for c in range(1, 7+1):
    niver = int(input('Digite o ano de nascimento da {}º pessoa: ' .format(c)))
    idade = atual - niver
    if idade >= 21:
        cont1 += 1
    else:
        cont2 += 1
print('{} pessoas ja antigiram a maioridade e {} pessoas não antigiram. '.format(cont1, cont2))

