from random import randint
totj = 0
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
    if pi == "P":
        if total % 2 == 0:
            totj += 1
            print("Você venceu!")
        else:
             print("você perdeu!")
    elif pi == "I":
        if total % 2 == 1:
            totj += 1
            print("você venceu!")
        else:
            print("Voce perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"O jogador ganhou {totj} vezes")

