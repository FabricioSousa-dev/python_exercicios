numeros = []
pares = []
impares = []
while True:
    n = int(input("Digite um número: "))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

#2 forma:
'''num = list()
pares = list()
impares = list()

while True:
    num.append(int(input("Digite um valor: ")))

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)'''

print(f"A lista com os números é {numeros}")
print(f"Os números pares são {pares}")
print(f"Os números impares são {impares}")