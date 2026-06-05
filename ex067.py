cont = 0
while True:
    n = int(input("Quer a ver a tabuada de qual número? "))
    if n <= 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
        while cont < 10:
            cont += 1
            print(f'{n} x {cont} = {n * cont}')

print("fim")


