pessoas = dict()
lista = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input("Nome: ")).strip().upper()
    pessoas['Idade'] = int(input("Idade: "))
    soma += pessoas['Idade']
    sexo = str(input("Sexo: [M/F]")).strip().upper()[0]

    while sexo not in "FM":
        print("ERRO! Digite apenas M ou F.")
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]

    pessoas['Sexo'] = sexo
    lista.append(pessoas.copy())


    opc = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if opc == "N":
        break


media = soma/ len(lista)

print("-=" * 30)
print(f"A)Tem {len(lista)} pessoas cadastradas.")
print(f"B)A média de idade do grupo é {media:5.2f} anos.")
print(f"C)As mulheres cadastradas foram: ",end='')
for m in lista:
    if m["Sexo"] == "F":
        print(f" {m['Nome']} ", end='')
print()
print(f"D)A lista de pessoas acima da média:")
for p in lista:
    if p['Idade'] > media:
        print(f"Nome = {p['Nome']}; sexo = {p['Sexo']}; idade = {p['Idade']} ")
print("<<ENCERRADO>>")


