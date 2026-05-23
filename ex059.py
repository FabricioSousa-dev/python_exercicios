opcao = 0
while opcao != 5:
     valor1 = int(input("Digite o primeiro valor: "))
     valor2 = int(input("Digite o segundo valor: "))
     opcao = str(input("Qual a sua opção?"))
     print(''''Você quer?
              [1] somar
              [2] multiplicar
              [3] maior
              [4] novos numeros
              [5] sair do programa''')
     if opcao == 1:
         print("{} + {} = {}".format(valor1, valor2, valor1 + valor2))
     if opcao == 2:
         print("{} * {} = {}".format(valor1, valor2, valor1 * valor2))
     if opcao == 3:
     



