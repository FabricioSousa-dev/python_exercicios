v = int(input("Qual a distãncia de uma viagem? "))


if v <= 200:
     m = (v * 0.50)
     print("O preço da passagem é R$ {:.2f}".format(m))

else :
    m = (v * 0.45)
    print("O preço da passagem foi R$ {:.2f}".format(m))
