Casa = float(input("Qual o valor da casa? "))
Salario = float(input("Qual o seu salário? "))
Anos = int(input("Em quantos anos vai pagar? "))

prestação = Casa / (Anos * 12)
minimo = Salario * 30/100

print("Para pagar uma casa de R${:.2f} em {} anos, ".format(Casa,Anos, end=''))
print( "a prestação será R${:.2f}".format(prestação))
if prestação <= minimo:
    print("Emprestimo pode ser aprovado!")
else:
    print("Emprestimo negado!")
