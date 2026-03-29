n = float(input("Qual o seu salário? "))

if n > 1250:
    a = n * 1.1
    print("Após o aumento de 10% o seu salário fica por {:.2f}".format(a))
else:
    a = n * 1.15
    print("Após o aumento de 15% o seu salário fica por {:.2f}".format(a))