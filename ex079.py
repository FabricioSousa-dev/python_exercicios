lista = []

while True:
    valor = int(input("Digite um valor: "))

    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado")
    else:
        print("Valor duplicado")

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()

    if resp == "N":
        break

print("-=" * 30)
lista.sort()
print(f"Os valores digitados foram: {lista}")


