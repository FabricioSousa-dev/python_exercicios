a1 = int(input("Digite um número inteiro: "))
tot = 0

for c in range(1, a1 + 1):
    if a1 % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else :
        print("\033[31m", end=" ")
    print("{} ".format(c), end=" ")
print("\n\033[mO número {} foi dívisivel por {} vezes".format(a1,tot))
if tot == 2:
    print("Por isso ele é PRIMO!")
else:
    print("Por isso ele não é PRIMO!")