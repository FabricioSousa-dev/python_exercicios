from random import randint
totj = 0
totp = 0
while True:
    print("==" * 30)
    print("JOGO DA ADIVINHAÇÃO")
    print("==" * 30)
    n = int(input("Digite um numero: "))
    if n < 0:
        break
    pi = input("Impat ou par[i/p] ").upper().strip()[0]

    while pi not in "IP":
        print("Valor digitado inválido!")
        pi = input("Impat ou par[i/p] ").upper().strip()[0]

    computador = randint(1, 10)

    total = n + computador

    print(f"O jogador escolheu {n} e o computador {computador} no total é {total} ")
    if total % 2 == 0:
        resultado = "P"
        print("È par!")
    else:
        resultado = "I"
        print("È ímpar!")
    if pi == resultado:
        print("O JOGADOR GANHOU")
        totj += 1
    else:
        print("O COMPUTADOR GANHOU!")
        totp += 1
        break
print(f"O jogador ganhou {totj} vezes e o computador ganhou {totj} vezes")

