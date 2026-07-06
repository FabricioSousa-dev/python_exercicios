from operator import itemgetter
from random import randint

dados = dict()
for p in range(1,5):
    dados[f'jogador{p}'] = randint(1,6)
for j in dados:
    print(f'{j} tirou {dados[j]}')
print("Ranking dos jogadores:")
for k,v in sorted(dados.items(), key=itemgetter(1), reverse=True):
    print(f'{k} tirou {v}')