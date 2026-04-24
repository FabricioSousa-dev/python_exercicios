import math
vc = float(input("Qual o valor da casa? "))
s = float(input("Qual o seu salário? "))
y = int(input("Em quantos anos vai pagar? "))

meses = y * 12
pm = vc/meses
la = s * 0.30

if pm <= la :
    print("Emprestimo aprovado!")
    print("Valor da prestação: R$ {:.3f} por mês".format(pm))
    print("limite màximo de renda: R$ {:.2f}".format(la))
else:
    print("Emprestimo negado!")
