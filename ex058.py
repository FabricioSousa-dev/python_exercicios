from random import randint
computer = randint(0, 10)
c = 1
total = 0
totv = 0
totp = 0
while c != computer:

    computer = randint(0, 10)
    p = int(input("Digite um numero de 0 a 10: "))
    if p == computer:
        print("Meus parábens você acertou!")
        total +=1
        totv += 1
        break
    else:

        print("Menos... Tente mais uma vez")
        total += 1
        continue
print("De {} tentativas vc acertou {}".format(total,totv))













