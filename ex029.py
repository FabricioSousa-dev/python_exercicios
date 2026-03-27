v = int(input("Qual a  velocidade do seu veículo? "))
m = (v - 80) * 7.00

if v > 80:
 print("Você foi multado!")
 print("Em {:.2f}R$".format(m))
else:
 print("Siga seu caminho!")
