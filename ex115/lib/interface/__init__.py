def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU DO SISTEMA')
    c = 1
    for item in lista:
        print(f'{c} -- {item}')
        c += 1
    print(linha())
    opc = leiaInt('Escolha uma opção: ')
    return opc