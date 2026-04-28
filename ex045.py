from random import choice

j = str(input("Qual a sua jogada?"))
lista = ["pedra", "papel", "tesoura"]


sorteando = choice(lista)
print("Sua escolha {} ".format(j))
print("Computador jogou {}".format(sorteando))
