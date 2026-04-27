from datetime import date
id = int(input("Digite o ano de nascimento: "))
atual = date.today().year
c = atual - id

if c <= 9:
    print("O atleta tem {} anos, sua categoria é mirim".format(c))
elif c <= 14:
    print("O Atleta tem {} anos, sua categoria é infantil ".format(c))
elif c <= 19:
    print("O atleta tem {} anos, sua categoria é junior ".format(c))
elif c <= 20:
    print("O atleta tem {} anos, sua categoria é sênior ".format(c))

else:
    print("O atleta tem {} anos, sua categoria é master".format(c))
