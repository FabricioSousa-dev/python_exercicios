a = int(input("Qual o comprimento da primeira reta? "))
b = int(input("Qual o comprimento da segundo reta? "))
c = int(input("Qual o comprimento da terceira reta? "))


if a == b and a == c and b == a and b == c and c == a and c == b:
    print("É equilátero")
elif a == b or a == c or b == c or c == a:
    print("Isoceles")
else:
    print("Escaleno")






