from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(0,5):
        n = randint(0,10)
        lista.append(n)
        sleep(0.5)
        print(f" {n} ", end='', flush=True)
        sleep(0.5)
    print("Pronto!")

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"Soamndo os valores pares de {lista} é {soma}")

numeros = list()
sorteia(numeros)
somaPar(numeros)







