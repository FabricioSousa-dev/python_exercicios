'''n = " "
cont = soma = maior = menor = 0
media = 0


while True:
    cont += 1
    n =int(input("Digite um valor: "))
    soma += n

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n



    if opcao == "N":
        break
if cont > 0:
    media = soma / cont
else:
    media = 0
print("Tem {} valores digitados, a média foi {}".format(cont,media))
print("O maior número digitado foi {} é o menor foi {}".format(maior,menor))
'''
#2 solução:

resp = "s"
soma = quant = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

média = soma / quant
print("Tem {} valores digitados, a média foi {}".format(quant,média))
print("O maior número digitado foi {} é o menor foi {}".format(maior,menor))









