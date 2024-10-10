def escreva(txt):
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))


txt = str(input('Digite uma frase: ')).upper().strip()
escreva(txt)