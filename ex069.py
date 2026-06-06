menoridadeP = 0
maioridadeP = 0
maioridadeH = 0
maioridadeM = 0
while True:
    print("-"*30)
    print("CADASTRE UMA PESSOA")
    print("-"*30)

    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

    print("-"*30)

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    while opcao not in "SN":
        print("Opcao invalida, tente novamente.")
        idade = int(input("Digite sua idade: "))
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

    if opcao == "N":
        break
    else:
        if opcao == "S":
            continue
   




print(f"Tem {maioridadeP} pessoas com mais de 18 anos.")