peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / altura ** 2
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta \033[4;31mabaixo do peso\033[m, procure os médicos. ')
elif 18.5 <= imc < 25:
    print('Você esta no peso ideal, \033[1;32mparabens\033[m. ')
elif 25 <= imc <= 30:
    print('Você esta na \033[33mpré-obesidade\033[m, procure melhorar os seus hábitos. ')
elif 30 <= imc < 40:
    print('Você esta \033[1;31mobeso\033[m, procure os médicos antes que seja tarde. ')
else:
    print('Você esta com \033[4;30mOBESIDADE MÓRBIDA\033[m, \033[31mprocure os médicos com urgência!\033[m ')
