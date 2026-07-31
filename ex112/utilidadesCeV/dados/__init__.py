def leiaDinheiro(mgs):
    '''

    :param mgs: valor inteiro.
    :return: retorna o valor inteiro verificado.
    '''
    ok = False
    valor = 0
    while True:
        p = input(mgs)
        if p.isnumeric():
            valor = float(p)
            ok = True
        else:
            if p.isalpha():
                print("Erro, digite apenas um número")
            elif p.strip() == '':
                print("Erro! valor invalido!")
            elif ',' in p:
                p = p.replace(',', '.')
                valor = float(p)
                ok = True
            elif '.' in p:
                valor = float(p)
                ok = True
            else:
                print("Erro! valor invalido!")
        if ok:
            break
    return valor