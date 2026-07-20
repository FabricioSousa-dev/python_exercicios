'''help(len)
print(input.__doc__)'''

def contador(i,f, p):
    '''
    -->Faz uma contegem do inicio até o fim do programa
    :param i:inicio da contegem
    :param f:fim da contegem
    :param p:passo da contegem
    :return:sem retorno
    Função criada por Gustavo Guanabara do canal curso em vídeo.
    '''
    c = i
    while c <= f:
        print(f" {c} ",end=" ")
        c += p
    print("Fim")




contador(2,10,2)
help(contador)