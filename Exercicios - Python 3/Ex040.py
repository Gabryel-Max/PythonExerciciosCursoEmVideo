nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\033[4;31mREPROVADO\033[m')
elif 7 > media >= 5:
    print('\033[4;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
