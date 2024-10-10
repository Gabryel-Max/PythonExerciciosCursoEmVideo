def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mDigite um valor inteiro válido.\033[m  ')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário decidiu não informar os dados.\033[m ')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mDigite um valor real. \033[m  ')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mO usuário decidiu não informar os dados.\033[m ')
        else:
            return n


num1 = leiaInt('Digite um valor inteiro: ')
num = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num1} ')
print(f'O valor real digitado foi {num}')
