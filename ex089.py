boletim = []

alunos = list()
while True:
    alunos.append(str(input("Nome do aluno: ")))
    alunos.append(float(input("Nota1: ")))
    alunos.append(float(input("Nota2: ")))
    boletim.append(alunos[:])
    alunos.clear()
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("-"*30)
print("No Nome        media ")
for i,n in enumerate(boletim):
    media = (n[1]+n[2])/2
    print(f"{i} {n[0]:<5}{media:>9}")
while True:
    m = int(input("Mostrar as notas de qual aluno? "))
    if m == 999:
        break
    else:
        print(f"Nome: {boletim[m][0]:<10} Nota1: {boletim[m][1]:.1f} Nota2: {boletim[m][2]:.1f}")

