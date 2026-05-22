sexo = 0

while sexo != "Mm" and sexo != "Ff":
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    if sexo == "M"or sexo == "F":
        print("Sexo valido")
    else:
        print("Sexo invalido")
        print("Continue!")
        continue
