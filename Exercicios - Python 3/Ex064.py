numero = cont = soma = 0
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('A quantidade de números digitados foi {} e a soma de tudo deu \033[35m{}\033[m '.format(cont - 1, soma))
