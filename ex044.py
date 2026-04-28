R = float(input("Qual o valor do produto? R$ "))
p = input("Qual o produto? ")
f = input("Qual a forma de pagamento? ")


if f.lower() == "dinheiro" or f.lower() == "cheque":
    d = R * 0.10
    pf = R - d
    print("\nForma de pagamento: {}".format(f))
    print("O produto {} custa R$ {:.2f}, você ganhou R$ {:.2f} de desconto (10%)".format(p, R, d))
    print("O preço final fica R$ {:.2f}".format(pf))


elif f.lower() == "cartão":
    parcelas = int(input("Quantas parcelas? "))


    if parcelas == 1:
        d = R * 0.05
        pf = R - d
        print("Preço final à vista no cartão: R$ {:.2f}".format(pf))


    elif parcelas == 2:
        pa = R / 2
        print("O produto {} custa R$ {:.2f} (sem desconto)".format(p, R))
        print("O cliente paga 2 parcelas fixas de R$ {:.2f}.".format(pa))


    else:
        total_com_juros = R * 1.20
        pa = total_com_juros / parcelas
        print("O produto {} com 20% de juros fica R$ {:.2f}".format(p, total_com_juros))
        print("O cliente paga {} parcelas de R$ {:.2f}.".format(parcelas, pa))

else:
    print("Forma de pagamento não reconhecida.")










