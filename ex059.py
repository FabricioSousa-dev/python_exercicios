n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
     print(''''
     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] maior 
     [ 4 ] novos numeros
     [ 5 ] sair do programa''')
     opcao = int(input("Qual a sua opção? "))

     if opcao == 1:
        s = n1 + n2
        print("{} + {} = {}".format(n1, n2, s))
     elif opcao == 2:
        m = n1 * n2
        print("{} * {} = {}".format(n1, n2, m))
     elif opcao == 3:
         if n1 > n2:
             print("{} é maior que {}".format(n1,n2))
         else:
             print("{} é menor que {}".format(n1,n2))
     elif opcao == 4:
          n1 = int(input("Digite o primeiro valor: "))
          n2 = int(input("Digite o segundo valor: "))
     elif opcao == 5:
         print("Finalizando...")
     else:
        print("Opção invalida!")
        print("=*=" * 10)
print('FIM DO PROGRAMA')
