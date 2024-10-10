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

num = leiaInt('Digite um valor inteiro: ')
print(f'\033[34mO valor digitado foi {num}\033[m')