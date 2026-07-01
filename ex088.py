from random import randint


print("==="*30)
print("Jogo da SORTE")
print("==="*30)

jogar = int(input("Quantos jogos deseja jogar? "))
print(f"------Sorteando {jogar} jogos--------")
for c in range(jogar):

    num = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    num.sort()
    print(f"Jogo {c+1}: {num}")

