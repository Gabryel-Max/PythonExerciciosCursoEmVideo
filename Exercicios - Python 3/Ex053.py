frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {} '.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
