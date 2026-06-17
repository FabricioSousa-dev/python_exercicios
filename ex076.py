Listagem = ("Café",2.00,
            "Banana",1.75,
            "Feijão",6.00,
            "Maçã",3.00)


print("=="*20)

print("LISTA DE PRODUTOS")
print("=="*20)

for pos in range(0,len(Listagem)):
   if pos % 2 == 0:
      print(f"{Listagem[pos]:.<30}",end=" ")
   else:
      print(f"R${Listagem[pos]:>7.2f}")