alunos = dict()

alunos['Nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'media: '))

if alunos['media']>= 7:
    print("A situação é que está aprovado! ")
elif alunos['media'] >= 5:
    print("Em recuperação")
else:
    print("A situaçao é reprovado! ")
for k,v in alunos.items():
    print(f"{k} é igual a {v}")
