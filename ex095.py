times = list()

while True:
    futebol = dict()
    futebol['Nome'] = str(input("Nome do jogador: "))
    futebol['Partidas'] = int(input("Quantidade de partidas: "))
    gols = list()
    total = 0

    for c in range(0, futebol['Partidas']):
        gols.append(int(input(f"Quantos gols na partida {c}? ")))
        total += gols[c]

    futebol['Gols'] = gols
    futebol['Total de gols'] = total
    times.append(futebol)

    opc = ' '
    while opc not in "SN":
        opc = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if opc == "N":
        break

print("=-"*30)
print(f"{'cod':<5}{'nome':<15}{'gols':<15}{'total':<10}")
print("-"*45)
for k, v in enumerate(times):
    print(f"{k:<5}{v['Nome']:<15}{str(v['Gols']):<15}{v['Total de gols']:>10}")

while True:
    m = int(input("Mostra os dados do jogador (999 para parar): "))
    if m == 999:
        print("=-"*30)
        print("Finalizando...")
        break
    elif m >= len(times):
        print(f"Não existe um jogador com codigo {m}")
    else:
        print(f"         --LEVANTAMENTO DO JOGADOR {times[m]['Nome']}            ")
        for c, g in enumerate(times[m]['Gols']):
            print(f"No jogo {c} fez {g} gols")