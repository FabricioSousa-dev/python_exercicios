def metade(num=0, formato=False):
    '''

    :param num: Recebe um número inteiro
    :param formato: Parametro se vai ou não retornar o valor formatado
    :return: valor formatado
    '''
    vf = num / 2
    return vf if formato is False else moeda(vf)


def dobro(num=0, formato=False):
    '''

    :param num: Numero inteiro
    :param formato: parametro
    :return: Valor formatado
    '''
    vf = num * 2
    return vf if formato is False else moeda(vf)


def aumentar(num=0, taxa=0, formato=False):
    '''

    :param num: numero inteiro
    :param taxa: taxa de aumento
    :param formato: condição de aumento
    :return: retorna o valor formatado
    '''
    vf = num + (num * taxa / 100)
    return vf if formato is False else moeda(vf)


def diminuir(num=0, taxa=0, formato=False):
    '''

    :param num: numero inteiro
    :param taxa: taxa de diminuir
    :param formato: condiço de diminuir
    :return: retorna o valor formatado
    '''
    vf = num - (num * taxa / 100)
    return vf if formato is False else moeda(vf)


def moeda(num=0, moeda='R$'):
    '''

    :param num: numero inteiro
    :param moeda: cifrão da moeda
    :return: retorna o valor formatado
    '''
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0, au=0, di=0):
    '''
    Resume todas as funções
    :param num: o valor do resumo
    :param au: o valor do aumento
    :param di: o valor do diminuir
    :return: Não retorna o valor formatado
    '''
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Analisando o valor:\t{moeda(num)}")
    print(f"A metade :\t\t\t{metade(num, True)}")
    print(f"O dobro :\t\t\t{dobro(num, True)}")
    print(f"Aumentando em {au}%:\t{aumentar(num, au, True)}")
    print(f"Diminuindo em {di}%:\t{diminuir(num, di, True)}")
    print("-"*30)