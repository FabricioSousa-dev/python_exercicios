from datetime import datetime
i = int(input("Digite o ano de nascimento: "))
agora = datetime.today().year

b = agora - i

if b == 18:
    print("Você pode se alistar!")
elif b < 18:
    saldo = b - 18
    print("Você ainda não pode se alistar!")
    print("Falta {} ano ".format(saldo))
else:
    print("Você ja passou da idade,se aliste o quanto antes!")
