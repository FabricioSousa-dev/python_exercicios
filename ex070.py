total = mais = menor = cont =  0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    cont += 1

    total += preco

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        mais += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total}')
print(f"{mais} produto(s) tem um preço mais que 1000")
print(f"O produto mais barato foi {barato} custa R${menor:.2f}")

