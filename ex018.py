import math
ângulo = float(input("Digite um ângulo: "))
seno = math.sin(math.radians(ângulo))
conseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print("O ângulo {} tem o seno de {:.2f},conseno de {:.2f} e tangente de {:.2f}".format(ângulo,seno,conseno,tangente))


3