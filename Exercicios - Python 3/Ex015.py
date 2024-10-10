km = float(input('Quantos quilometros foram rodados: '))
dia = float(input('Quantos dias foram alugados: '))
rf = (dia * 60) + (km * 0.15)
print('O carro rodou {}Km e ficou {} dias alugados, o valor a se pagar ao total é de R${:.2f} '.format(km, dia, rf))
