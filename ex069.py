m = f = maior = menor = 0
while True:
    print("-"*30)
    print("CADASTRE UMA PESSOA")
    print("-"*30)

    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

    print("-"*30)

    if idade >= 18:
        maior += 1
    if sexo == "M":
        m += 1
    elif sexo == "F" and  idade < 20:
        f += 1
        menor += 1






    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    while opcao not in "SN":
        print("Opcao invalida, tente novamente.")
        sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

    if opcao == "N":
        break
    elif opcao == "S":
        continue

print("-"*30)
print(f"Total de homens cadastardos: {m}")
print(f"Total de mulheres: {f}")
print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"Total de mulheres com menos de 20 anos: {menor}")