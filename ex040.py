n1 = float(input("Informa a sua primeira nota: "))
n2 = float(input("Informe a sua segunda nota: "))

m = (n1 + n2)/2

if m >= 7.0:
    print("Você foi aprovado")
elif m >= 5.0 or m <= 6.0:
    print("Que pena você está em recuperação!")
else:
    print("Você foi reprovado!")