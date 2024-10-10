def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno com {largura}x{comprimento} é de {a}m² ')
def lin():
    print('-'*50)


print('Controle de Terrenos ')
lin()
largura = float(input('Largura da parede: '))
comprimento = float(input('Comprimento da parede: '))
lin()
area(largura, comprimento)
lin()