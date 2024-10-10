from datetime import date
atual = date.today().year
dados = dict() #APOSENTA DEPOIS DE 35 ANOS DE COLABORAÇÃO
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nasc: '))
dados['idade'] = atual - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
idade = atual - dados['idade']
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - atual)
print('='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
