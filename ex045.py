from random import choice

j = str(input("Qual a sua jogada?"))
lista = ["pedra", "papel", "tesoura"]


sorteando = choice(lista)
print("Sua escolha {} ".format(j))
print("Computador jogou {}".format(sorteando))

if j == sorteando:
    print("EMPATE")
elif j == "pedra"  and sorteando =="tesoura":
    print("JOGADOR VENCE")
elif j == "papel" and sorteando == "pedra":
    print("JOGADOR VENCE")
elif j == "tesoura" and sorteando == "papel":
    print("JOGADOR VENCE")
else:
    print("O computador venceu")

