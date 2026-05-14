from datetime import datetime, date
maioridade = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    i = int(input('Digite o ano de nascimento: '))
    maior = maioridade - i
    if maior >= 18:
        totmaior += 1
    else :
        totmenor += 1
print("Ao todo tivemos {} pessoas de maior".format(totmaior))
print("E tivemos {} pessoas de menor".format(totmenor))








