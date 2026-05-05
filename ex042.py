a = int(input("Qual o comprimento da primeira reta? "))
b = int(input("Qual o comprimento da segundo reta? "))
c = int(input("Qual o comprimento da terceira reta? "))

if a + b > c and a + c > b and b + c > a:
    print("Forma um trângulo!")

    if a == b == c:
        print("É equilátero")
    elif a !=b !=c !=a:
            print("Escaleno")
    else:
     print("Isosceles")

else:
    print("Não forma um triângulo!")







