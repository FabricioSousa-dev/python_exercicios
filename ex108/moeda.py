def metade(num):
    return num / 2

def dobro(num):
    return num *2

def aumentar(num,taxa=0):
    vf = num + (num * taxa)
    return vf

def diminuir(num,taxa=0):
    vf = num - (num * taxa)
    return vf


def moeda(num):
    valor = f'{num:.2f}'
    return f"R${valor}"