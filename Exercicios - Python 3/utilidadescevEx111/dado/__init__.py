def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro \033[31m\"{entrada}\"\033[m é um preço inválido! ')
        else:
            valido = True
            return float(entrada)
