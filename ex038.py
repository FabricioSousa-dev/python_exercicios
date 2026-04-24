n1 = int(input(("Qual o primeiro valor? ")))
n2 = int(input(("Qual o segundo valor? ")))

if n1 > n2:
    print("O {} é maior que o {}".format(n1, n2))
elif n2 > n1:
    print("O {} é maior que o {}".format(n2, n1))
else:
    print("Os dois são iguais ")
