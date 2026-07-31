from ex107 import moeda
p = float(input(("Digite um preço:  R$")))
print(f"A metade de R${p} é {moeda.metade(p)}")
print(f"O dobro de R${p} é {moeda.dobro(p)}")
print(f"Aumentando em 10%, temos R${moeda.aumentar(p, 10)}")
print(f"Diminuindo em 15%, temos R${moeda.diminuir(p, 15)}")