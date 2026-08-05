from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar pessoas", "Sair do sistema" ])
    if resposta == 1:
        cabecalho("Opção 1")
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("Opção 2")
        criarArquivo(arq)
    elif resposta == 3:
        cabecalho("Sair do sistema")
        break
    else:
        print("Erro! opção invalida!")
