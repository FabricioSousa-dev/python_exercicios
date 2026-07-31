def metade(num=0,formato=False):
    '''

    :param num: Recebe um número inteiro
    :param formato: Parametro se vai ou não retornar o valor formatado
    :return: valor formatado
    '''
    vf = num / 2
    return vf if formato is False else moeda(vf)


def dobro(num=0,formato=False):
    '''

    :param num: Numero inteiro
    :param formato: parametro
    :return: Valor formatado
    '''

    vf = num * 2
    return vf if formato is False else moeda(vf)

def aumentar(num=0,taxa=0,formato=False):
    '''

    :param num: numero inteiro
    :param taxa: taxa de aumento
    :param formato: condição de aumento
    :return: retorna o valor formatado
    '''

    vf = num + (num * taxa/100)
    return vf if formato is False else moeda(vf)

def diminuir(num=0,taxa=0,formato=False):
    '''

    :param num: numero inteiro
    :param taxa: taxa de diminuir
    :param formato: condiço de diminuir
    :return: retorna o valor formatado
    '''
    vf = num - (num * taxa/100)
    return vf if formato is False else moeda(vf)


def moeda(num=0,moeda='R$'):
    '''

    :param num: numero inteiro
    :param moeda: cifrão da moeda
    :return: retorna o valor formatado
    '''
    return f'{moeda}{num:.2f}'.replace('.',',')