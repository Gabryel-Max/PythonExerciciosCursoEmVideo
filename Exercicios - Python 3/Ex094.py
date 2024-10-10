lista = list()
dicionario = dict()
soma = media = 0
while True:
    dicionario['nome'] = str(input('Nome: ')).capitalize()
    dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if dicionario['sexo'] not in 'MF':
        print('Digite apenas M ou F.')
        dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
print('='*45)
print(f'=> O grupo tem {len(lista)} pessoas. ')
media = soma / len(lista)
print(f'=> A média de idade é {media:5.2f} anos. ')
print(f'=> As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()
print('='*45)