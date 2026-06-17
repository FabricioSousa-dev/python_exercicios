n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite outro valor: "))
n4 = int(input("Digite outro valor: "))

valores = (n1, n2, n3, n4)

print(f"O valore digitados são {valores}")
print("="*40)
print(f"O valor 9 apareceu {valores.count(9)} vezes")
if 3 in valores:
 print(f"O valor 3 está na posição {valores.index(3)}")
else:
    print("Não tem um número 3!")
print("Os valores pares digitados foram ", end="")

for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
