from ex115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Erro ao criar o arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(a.read())
    finally:
        a.close()


def criarArquivo(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na abertura do arquivo")
    finally:
        a.write(f'{nome};{idade}\n')