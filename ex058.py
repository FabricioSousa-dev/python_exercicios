from operator import truediv
from random import randint
computador = randint(0,10)
print("Olá sou seu computador vou pensar em um numero entre 0 e 10")

acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais....tente mais uma vez!")
        elif jogador > computador:
            print("Menos....tente mais uma vez!")
print("Acertou com {} palpites!".format(palpite))














