from random import randint
c = 1
computer = randint(0, 5)
tentativas = 0

while c != computer:
    print("what number am i thinking of? ")
    player = int(input("Is it? "))
    computer = randint(1, 10)
    if player > 0:

        if player == computer:
            print("You win!")
            tentativas += 1
            continue

        else:
            print("Computer wins!")
            tentativas += 1
            continue
    else:
        print("Valor invalido!")

print("{} tentativa(s)!".format(tentativas))









