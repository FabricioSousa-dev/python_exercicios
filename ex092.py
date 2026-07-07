from datetime import date

pessoa = dict()
pessoa['Nome'] = str(input("Nome: "))
Idade = int(input("Ano de nascimento: "))
pessoa['Ctps'] = int(input("Carteira de trabalho(0 não tem): "))
atual = date.today().year
pessoa['Idade'] = atual - Idade


if pessoa['Ctps'] == 0:
    print("=-"*30)
    for k,v in pessoa.items():
        print(f"O {k} tem o valor {v}.")
else:
    pessoa['Ano de contratação'] = int(input("Ano de contratação: "))
    pessoa['Salario'] = float(input("Salario:R$  "))
    aposentadoria = (pessoa['Ano de contratação'] + 35) - Idade
    pessoa['Aposentadoria'] = aposentadoria
    for k, v in pessoa.items():
        print(f"{k} tem o valor {v}")






