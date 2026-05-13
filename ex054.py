from datetime import datetime, date

for c in range(1,8):
    i = int(input('Digite o ano de nascimento: '))
    maioridade = date.today().year - i
    if maioridade >= 18:
        print("{}ª pessoa é de maior".format(c))
    else :
        print("{}ª pessoa é de menor".format(c))


print('FIM')
print("TEste")



