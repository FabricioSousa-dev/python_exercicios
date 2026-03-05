n1 = str(input("Digite seu nome completo: ")).strip()
nome = n1.split()
print("primeiro: {}".format(nome[0]))
print("último: {}".format(nome[len(nome)-1]))
