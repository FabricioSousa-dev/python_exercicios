brasilerão = ("Palmeiras", "Flamengo", "Fluminense", "Atletico-Paraense", "RB-Bragantino",
              "Bahia", "Curitiba", "São-Paulo", "Atletico-MG","Corinthians",
              "Cruzeiro", "Botafogo", "Vitoria", "Internacional", "Santos",
              "Gremio", "Vasco da gama","Remo","Mirassol", "Chapecoense-sc")
print(f"Lista dos times do brasileirão {brasilerão}")

print("=="*40)

print(f"Os 5 primeiros colocados são {brasilerão[0:5]}")

print("=="*40)

print(f"Os últimos 4 colocados {brasilerão[-4:]}")

print("=="*40)

print(f"Os times em ordem alfabetica {sorted(brasilerão)}")

print("=="*40)

print(f"Chapecoense está no {brasilerão.index('Chapecoense-sc') + 1}º lugar")

