futebol = dict()
futebol['Nome'] = str(input("Nome do jogador: "))
futebol['Partidas'] = int(input("Quantidade de partidas: "))
total = 0
futebol['Gols'] = gols = list()

if futebol['Partidas'] > 0:
    for c in range(0,futebol['Partidas']+1):
        gols.append(int(input(f"Quantos gols na partida {c}: ")))
        total += gols[c]
        futebol['Total de gols'] = total
print("=-"*30)
print(futebol)
print("=-"*30)
for k, v in futebol.items():
    print(f"O campo {k} tem o valor {v}")
print("=-"*30)
print(f"O jogador {futebol['Nome']} jogou {futebol['Partidas']} partidas. ")
for p in range(0,futebol['Partidas']+1):
    print(f"=> Na partida {p} fez {futebol['Gols'][p]} gols.")
