cont18 = conthomens = contmulheres = 0
while True:
    idade = int(input('Idade : '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade < 20:
        contmulheres += 1
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'Quantidade de pessoas maiores de 18: {cont18} ')
print(f'Quantidade de homens cadastrados: {conthomens} ')
print(f'Quantidade de mulheres abaixo de 20: {contmulheres} ')

