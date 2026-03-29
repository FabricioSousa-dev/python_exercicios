a = int(input("Qual o comprimento da primeira reta? "))
b = int(input("Qual o comprimento da segundo reta? "))
c = int(input("Qual o comprimento da terceira reta? "))

if a + b > c and a + c > b and b + c > a:
    print("Forma um trângulo!")

else:
    print("Não forma um triângulo!")
