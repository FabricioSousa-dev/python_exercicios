'''boletim = []
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
print("="*30)
print(f'{"No":<4}{"NOME":<10}{"MÈDIA":>8}')
print("-"*30)
for i,n in enumerate(boletim):
    media = (n[1]+n[2])/2
    print(f"{i:<4}{n[0]:<10}{media:>8.1f}")
while True:
    m = int(input("Mostrar as notas de qual aluno? "))
    if m == 999:
        break
    else:
        print(f"Nome: {boletim[m][0]:<10} Nota1: {boletim[m][1]:.1f} Nota2: {boletim[m][2]:.1f}")'''

#2 forma:

ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    ficha.append([nome,nota1,nota2])
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
        break
print("-"*30)
print(f'{"No":<4}{"NOME":<10}{"MÈDIA":>8}')
print("-"*30)
for i,n in enumerate(ficha):
    print(f"{i:<4}{n[0]:<10}{media:>8.1f}")
while True:
    opc = int(input("Mostrar notas de qual aluno?(999 interrompe): "))
    if opc == 999:
        break
    elif opc <= len(ficha):
        print(f"Aluno {ficha[opc][0]},notas: {ficha[opc][1]} e {ficha[opc][2]}")
print("Finalizando...")

