from ex108 import moeda
p = float(input(("Digite um preço:  R$")))
print(f"A metade de {p} é {moeda.moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumentando em 10%, temos {moeda.aumentar(p, 0.10)}")
print(f"Diminuindo em 15%, temos {moeda.diminuir(p, 0.15)}")