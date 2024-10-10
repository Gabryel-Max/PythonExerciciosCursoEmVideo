numeros = 'zero' , 'um' , 'dois' , 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis' , 'dezessete' , 'dezoito' , 'dezenove' , 'vinte'
for contador in numeros:
    digite = int(input('Digite um número de 0 a 20 : '))
    if digite > 20 or digite < 0:
        print('Número invalido... Tente novamente ')
    else:
        print('O numero digitado foi {}'.format(numeros[digite]))
