totmaior = 0
totmenor = 0
for c in range(1,6):
    p = float(input("Digite o seu peso: "))
    if c == 1:
        totmaior += 1
    else:
        totmenor += 1
print("A {} pessoa é mais pesada da lista".format(totmaior))
print("A {} pessoa e mais leve da lista".format(totmenor))


