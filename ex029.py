v = int(input("Qual a  velocidade do seu veículo? "))
m = 7 * v

if v > 80:
 print("Você foi multado!")
 print("EM {}R$".format(m))
