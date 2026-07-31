def metade(num=0):
    vf = num/2
    return vf

def dobro(num=0):
    vf = num * 2
    return vf

def aumentar(num=0,taxa=0):
    vf = num + (num * taxa/100)
    return vf

def diminuir(num=0,taxa=0):
    vf = num - (num * taxa/100)
    return vf


def moeda(num=0,moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')