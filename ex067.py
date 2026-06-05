while True:
    n = int(input("Quer ver a tabuada de qual número? "))
    if n < 0:
        break

    cont = 0
    #for c in range(1,11):
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
    print("-" * 15)
print("PROGRAMA TABUADA ENCERRADO")