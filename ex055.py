for c in range(1,6):
    peso = float(input("Digite peso da {} pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
                menor = peso
print("O maior peso lido foi {}".format(maior))
print("O menor peso lido foi {}".format(menor))


