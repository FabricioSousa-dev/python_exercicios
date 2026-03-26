import random

print("Em qual número inteiro estou pensando? ")
p = int(input("Será que é? "))

print("Você acha que é {}".format(p))

num = random.randint(0, 5)

if p == num:
    print("você acertou!")

else:
    print("Errou!")

