lista = []

while True:
    lista.append(int(input("Digite um valor: ")))

    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]


    if resp == "N":
        break
print("-=" * 30)
print(f"Os números digitados foram {lista}")
print(f"Foram {len(lista)} números digitados na lista")
lista.sort(reverse=True)
print(f"A lista de forma decrescente {lista}")
if 5 in lista:
    print("O valor 5 foi digitado na lista!")
else:
    print("O valor 5 não foi digitado na lista!")