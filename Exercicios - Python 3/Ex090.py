dicionario = dict()
aprovado = reprovado = ''
for c in range(1):
    dicionario['nome'] = str(input('Nome: '))
    dicionario['media'] = float(input('Qual é a média: '))
print(f'Nome é igual a {dicionario["nome"]} ')
print(f'Média é igual a {dicionario["media"]} ')
if dicionario['media'] >= 7:
    print(f'A situação é igual a APROVADO')
else:
    print(f'A situação é igual a REPROVADO')
    print('Estude mais! ')
