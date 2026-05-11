s = 0
cont = 0
for c in range(1,7):
    n = int(input("Qual o {}ª valor: ".format(c)))
    if n % 2 == 0:
      s += n
      cont += 1
print("O somatorio de todos os {} valores é {} ".format(cont,s))





