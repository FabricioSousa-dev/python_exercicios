def factorial(num=0,show=False):
    '''
    -->Calcula o fatorial de um numero
    :param num: O valor do numero que vai ser calculado
    :param show: mostra o calculo do fatorial
    :return: retorna o factrio do numero
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
             print(f" x ",end='')
            else:
                print(" = ",end='')
        f*= c
    return f





n = int(input("Digite um número: "))
fact = factorial(n,show=True)
print(fact)


