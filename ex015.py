km = float(input("Quantos km o carro foi alugado? "))
dias = int(input("Quantos dias o carro foi alugado? "))
pd = (dias * 60) + (km * 0.15)
print("Pelos dias e km serão cobrados {:.2f}R$".format(pd))