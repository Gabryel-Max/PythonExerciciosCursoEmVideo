from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Novo Cadastro ')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print(f'\033[30mSaindo do sistema... Até logo!\033[m ')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m ')
    sleep(0.5)