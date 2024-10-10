soma = n = cont = 0
print('''[\033[34m999\033[m] SAIR DO PROGRAMA''')
while True:
    cont += 1
    n = int(input(f'Digite o {cont}º valor: '))
    if n == 999:
        cont -= 1
        break
    soma += n
print(f'A soma dos {cont} números deu {soma} ')
