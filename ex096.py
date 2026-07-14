def area(largura, comprimento):
    a = largura * comprimento
    print(f"O terreno tem {largura}x{comprimento} a área é {a}m2")


print('-'*30)
print(f'{"CONTADOR DE AREA":^30}')
print('-'*30)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)
