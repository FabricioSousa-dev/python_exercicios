totpreço = maisprodutos =  0
menorPreço = float("inf")
nomeMaisbarato = ' '
while True:
    print('-'*30)
    print("LOJA SUPER BARATÃO")
    print('-'*30)




    nome = str(input('Qual o nome do produto? '))
    preço = float(input("Qual o preço do produto? R$  "))



    totpreço += preço

    if preço >= 1000:
        maisprodutos += 1
    if preço < menorPreço:
        menorPreço = preço
        nomeMaisbarato = nome



    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f"O total gasto na compra é {totpreço} ")
print(f"Tem {maisprodutos} produtos que custam mais de R$1000 ")
print(f"O produto mais barato é {nomeMaisbarato} com o menor preço de {menorPreço} R$")
