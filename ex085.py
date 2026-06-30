num = [[],[]]
for c in range(1,8):
    valor = int(input(f"Digite {c}o. valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)

print("===="*30)
num[0].sort()
num[1].sort()
print(f"Os valores pares digitados foram {num[0]} ")
print(f"Os valores impares digitados foram {num[1]}")