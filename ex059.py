opcao = 0
print(''''Você quer?
             [1] somar
             [2] multiplicar
             [3] maior
             [4] novos numeros
             [5] sair do programa''')

while opcao != 5:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    opcao = str(input("Qual a sua opção? "))

    if opcao == "1":
         print("{} + {} = {}".format(valor1, valor2, valor1 + valor2))
    if opcao == "2":
         print("{} * {} = {}".format(valor1, valor2, valor1 * valor2))
    if opcao == "3":
         print("{} / {} = {}".format(valor1, valor2, valor1 / valor2))
    if opcao == "4":
         print("Você quer entrar com novos numeros?")
         r = str(input("Quer continuar?"))
         if r == "Ss":
             valor1 = int(input("Digite o primeiro valor: "))
             valor2 = int(input("Digite o segundo valor: "))
         else:
             print("OK")
             break
    if opcao == "5":
         print("Saindo do programa")
         break