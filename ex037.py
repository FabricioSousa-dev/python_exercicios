n = int(input("Digite um número inteiro: "))
print('Escolha sua base de conversão')
print("[ 1 ] para binário")
print("[ 2 ] para octal")
print("[ 3 ] para hexadecimal")

opcoes = int(input("Escolha sua base: "))
if opcoes == 1:
    print("{} para binário é {}".format(n,bin(n)[2:]))
elif opcoes == 2:
    print("{} em octal é {}".format(n,oct(n)[2:]))
elif opcoes == 3:
    print("{} para hexadecimal é {}".format(n,hex(n)[2:]))
else:
    print("Opção invalida!")