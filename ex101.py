
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 16:
        return f" Com {idade} anos, Voto Reprovado!"
    elif 16 <= idade < 18 or idade > 65:
        return f" Com {idade} anos, Voto Opcional!"
    else:
        return f" Com {idade} anos, Voto Obrigatorio!"



#programa principal
print("=="*30)
n = int(input("Digite o ano de nascimento: "))
print(voto(n))