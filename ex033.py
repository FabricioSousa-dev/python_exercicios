n1 = int(input("digite o primeiro número: "))
n2 = int(input("Digite o segundo: "))
n3 = int(input("Digite o terceiro: "))

if n1 > n2 and n1 > n3:
    print("{} é maior que {} e {}".format(n1, n2, n3))

elif n1 < n2 and n1 < n3:
    print("{} é menor que {} e {}".format(n1, n2, n3))

if n2 > n1 and n2 > n3:
    print("{} é maior que {} e {}".format(n2, n1, n3))

elif n2 < n1 and n2 < n3:
    print("{} é menor que {} e {}".format(n2, n1,n3))

if n3 > n1 and n3 > n2:
    print("{} é maior que {} e {}".format(n3, n1, n2))
elif n3 < n1 and n3 < n2:
    print("{} é menor que {} e {}".format(n3, n1, n2))


