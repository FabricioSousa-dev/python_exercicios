sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

while sexo not in "MmFf":
   sexo = str(input("dados invalidos por favor digite o sexo [M/F]: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
