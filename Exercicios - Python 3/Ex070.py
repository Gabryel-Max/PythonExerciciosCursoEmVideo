totalgasto = maisde1000 = nomeproduto = cont = precobarato = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    totalgasto += preco
    cont += 1
    if preco > 1000:
        maisde1000 += 1
    if cont == 1:
        nomeproduto = produto
        precobarato = preco
    if preco < precobarato:
        nomeproduto = produto
        precobarato = preco
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi: R${totalgasto:.2f} ')
print(f'Quantidade de produto de mais de R$1000: {maisde1000} ')
print(f'O produto mais barato foi {nomeproduto} que custa R${precobarato:.2f} ')
