contagem = ("zero","um","dois","três","quatro",
            "cinco","seis","sete","oito","nove",
            "dez","onze","doze","treze","quatorze",
            "quinze","dezesseis","dezessete","dezoito",
            "dezenove","vinte")

while True:
    p = int(input("Digite um número entre 0 e 20:  "))
    while p < 0 or p > 20:
        print("Tente novamente!")
        p = int(input("Digite um número entre 0 e 20:  "))
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
            break



print(f"O número que você digitou foi {contagem[p]}")


