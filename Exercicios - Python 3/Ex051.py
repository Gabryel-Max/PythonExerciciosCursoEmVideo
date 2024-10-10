prit = int(input('O primeiro termo é: '))
razao = int(input('A razão é: '))
decimo = prit + (11-1) * razao
for c in range(prit, decimo, razao):
    print(c, end=' ')