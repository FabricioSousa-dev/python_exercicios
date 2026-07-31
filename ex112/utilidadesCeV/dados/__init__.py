def leiaDinheiro(mgs):
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
            if p.strip() == '':
                print("Erro! valor invalido!")
            if '.' in p:
                p = p.replace('.', '.')
                valor = float(p)
                ok = True
            if ',' in p:
                p = p.replace(',',',')
                valor = float(p)
                ok = True

        if ok:
            break
    return valor