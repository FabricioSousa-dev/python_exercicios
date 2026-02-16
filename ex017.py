from math import sqrt,hypot

co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))
tp = sqrt(co ** 2 + ca ** 2)
#tp = hypot(co,ca)
print("O comprimento do triângulo retângulo é {:.2f}".format(tp))