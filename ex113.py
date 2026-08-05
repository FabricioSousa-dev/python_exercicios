def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mErro! digite um número inteiro')
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuario")
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mErro! digite um número float')
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuario")
            return 0
        else:
            return num




a = leiaInt("Digite um numero: ")
b = leiaFloat("Digite um numero: ")
print(f'O valor inteiro digitado foi {a} e float {b}')


