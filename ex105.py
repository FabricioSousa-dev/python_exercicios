def notas(*n, sit=False):
    '''
    -->Calcula a nota de um aluno.
    :param n: As notas dos alunos,uma ou mais.
    :param sit: A condição para mostrar a situação.
    :return: Retorna um dicionario com a nota do aluno.
    '''
    nota = dict()
    nota['Total'] = len(n)
    nota['Maior'] = max(n)
    nota['Menor'] = min(n)
    nota['Media'] = sum(n)/len(n)
    if sit:
        if nota['Media'] >= 7:
            nota['Situação'] = "Muito Bom"
        elif nota['Media'] >= 5:
            nota['Situação']= "Razoavel"
        else:
             nota['Situação']="Ruim"
    return nota


#programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
