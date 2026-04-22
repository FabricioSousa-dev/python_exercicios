from random import randint

print("what number am i thinking of? ")
player = int(input("Is it? "))

print("Do you think it is {}".format(player))

computer = randint(0, 5)

if player == computer:
    print("you correct!")

else:
    print("Damnit!")

