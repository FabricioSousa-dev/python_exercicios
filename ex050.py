s = 0
for c in range(0,6):
    n = int(input("Qual o valor: "))
    if n % 2 == 0:
      s += n
    else:
        print("{} é impar".format(n))
print("O somatorio de todos os valores é {} ".format(s))





