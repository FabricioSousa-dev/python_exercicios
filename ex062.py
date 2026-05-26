
a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))

decimo = a1 + (10 - 1) * r


while a1 < decimo:
    a1 += r
    print("{}".format(a1),end= " ")


    p = str(input("\nVocê quer ver mais termos? ")).upper()
    if p == "Ss":
        continue
    else:
        break







