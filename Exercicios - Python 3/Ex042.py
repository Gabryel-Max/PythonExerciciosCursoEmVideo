a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('É possivel formar um triângulo com esses segmentos!')
    if a == b == c:
        print('Esse triângulo é \033[1;36mEquilátero\033[m')
    elif a == b or a == c or b == c:
        print('Esse triângulo é \033[1;33mIsósceles\033[m' )
    else: #elif a != b != c != a (ASSIM TAMBEM FUNCIONA)
        print('Esse triângulo é \033[1;31mEscaleno\033[m' )
else:
    print('Não é possivel fazer um triângulo com esses segmentos.')