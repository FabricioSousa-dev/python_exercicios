valores = []
mai = men = 0
for cont in range(0, 5):
  valores.append(int(input(f"Digite {cont} valor: ")))
  if cont == 0:
    mai = men = valores[cont]
  else:
    if valores[cont] > mai:
      mai = valores[cont]
    if valores[cont] < men:
      men = valores[cont]

print("======="*20)
print(f"Foram digitados os valores {valores}")
print(f"O maior valor é {mai} nas posições ",end='')
for i, v in enumerate(valores):
    if v == mai:
      print(f"{i}....",end='')
print()
print(f"o menor valor é {men} nas posições ",end='')
for i,v in enumerate(valores):
    if v == men:
      print(f"{i}...",end="")
print()






