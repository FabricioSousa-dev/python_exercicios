cont = soma = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    cont += 1
    soma += n
    if n == 999:
        break
soma -= 999
print(f"Forma {cont} números digitados, a soma deles vale {soma}")
