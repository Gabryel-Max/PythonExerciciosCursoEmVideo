soma = 0
cont = 0
for c in range(1, 6+1):
    numero = int(input('Digite o {}º valor inteiro: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Você informou {} números PARES é a soma foi {} '.format(cont, soma))
