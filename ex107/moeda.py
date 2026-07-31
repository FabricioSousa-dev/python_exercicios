def metade(num):
    res = num / 2
    return res

def dobro(num):
    res = num *2
    return res

def aumentar(num,taxa=0):
    res = num + (num * taxa/100)
    return res

def diminuir(num,taxa=0):
    res = num - (num * taxa/100)
    return res
