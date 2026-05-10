n1 = int(input("Qual o primeiro valor: "))
n2 = int(input("Qual o segundo valor: "))
n3 = int(input("Qual o terceiro valor: "))
n4 = int(input("Qual o quarto valor: "))
n5 = int(input("Qual o quinto valor: "))
n6 = int(input("Qual o sexto valor: "))
for c in range(0,7):
    if n1 % 2 == 0:
        print("{} é par".format(n1))
        if n2 % 2 == 0:
          print("{} é par".format(n2))
          if n3 % 2 == 0:
              print("{} é par".format(n3))
              if n4 % 2 == 0:
                  print("{} é par".format(n4))
                  if n5 % 2 == 0:
                      print("{} é par".format(n5))
                      if n6 % 2 == 0:
                          print("{} é par".format(n6))

print("Fim")

