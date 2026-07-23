def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! digite um número inteiro')
        if ok:
            break
        return valor


#programa principal
n = leiaInt("Digite um numero: ")
print(f"O número digitado foi {n}")