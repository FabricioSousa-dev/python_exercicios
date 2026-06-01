n = " "
cont = soma = 0
media = 0
maior = menor = 0

while True:
    cont += 1
    n =int(input("Digite um valor: "))
    soma += n

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()


    if opcao == "N":
        break
if cont > 0:
    media = soma / cont
else:
    media = 0

print("Você digitou {} números,a média entre eles foi {:.2f} ".format(cont,media))









