# 📘 Documentação — `python_exercicios`

> Guia de consulta rápida para revisar conceitos de Python praticados neste repositório.
> Feito para você "matar a dúvida" rápido: encontre o tema, veja o exemplo, veja o exercício correspondente no código.

---

## 1. Visão geral do repositório

Este repositório reúne exercícios progressivos de Python (padrão do curso "Curso em Vídeo"), organizados assim:

```
python_exercicios-master/
├── ex001.py ... ex106.py        → exercícios avulsos (1 arquivo = 1 exercício)
├── ex107/ ... ex110/            → exercícios com módulo próprio (moeda.py + teste.py)
├── ex111/ ... ex112/             → exercícios com pacotes (utilidadesCeV/, com subpacotes)
├── ex113.py, ex114.py             → tratamento de exceções (try/except/else/finally)
├── ex115/                         → projeto maior: sistema de cadastro com pacotes lib.interface e lib.arquivo
└── Scripys-python/               → desafios extras/soltos (Teste01, desafio01-03)
```

**Como executar qualquer exercício:**
```bash
python ex001.py
```

**Como executar os que usam módulo/pacote (ex107 a ex112, e ex115):**
Rode a partir da pasta `python_exercicios-master` (a pasta pai), não de dentro da subpasta, porque os arquivos importam como pacote (`ex115.lib.interface`, por exemplo):
```bash
# estando em python_exercicios-master/
python ex107/teste.py
python ex112/teste.py
python -m ex115.sistema
```

---

## 2. Trilha de aprendizado (o que cada faixa de exercícios ensina)

| Faixa | Tema | Destaques |
|---|---|---|
| ex001–ex008 | Entrada/saída, tipos e formatação | `input()`, `print()`, `.format()`, métodos de string como `.isnumeric()` |
| ex009–ex015 | Operadores aritméticos | tabuada, conversões (metros↔cm/mm), câmbio, desconto/aumento percentual |
| ex016–ex018 | Módulo `math` | `trunc`, `sqrt`, `hypot`, `sin/cos/tan` com `radians` |
| ex019–ex020 | Módulo `random` (parte 1) | `choice`, `shuffle` |
| ex021 | Extra (áudio) | `pygame` para tocar som — foge do escopo padrão do curso |
| ex022–ex027 | Strings avançado | `upper/lower/strip/count/find/rfind/split` |
| ex028–ex045 | Estruturas condicionais | `if/elif/else`, condições aninhadas, `and/or` |
| ex046–ex070 | Laços de repetição | `for`, `while`, `range()`, `break`, contadores/acumuladores, sentinela (999) |
| ex071 | Estudo de caso: saque bancário | divisão em cédulas com `while` aninhado |
| ex072–ex077 | Tuplas | indexação, fatiamento (`slice`), `sorted()`, `.index()`, `.count()` |
| ex078–ex089 | Listas | `.append()`, `.sort()`, `.insert()`, listas de listas (matriz), `enumerate()` |
| ex090–ex095 | Dicionários | `dict()`, `.items()`, dicionário dentro de lista, listas dentro de dicionário |
| ex096–ex105 | Funções | parâmetros padrão, `*args`, docstrings, retorno de valores/dicionários |
| ex106 | Cores no terminal + `help()` | códigos ANSI, função de "ajuda" interativa |
| ex107–ex110 | Módulos | separar funções em arquivo `moeda.py` e importar com `from ex107 import moeda` |
| ex111–ex112 | Pacotes | pastas com `__init__.py` (`utilidadesCeV/moeda`, `utilidadesCeV/dados`) |
| ex113–ex114 | Tratamento de exceções | `try/except/else/finally`, exceções específicas (`ValueError`, `KeyboardInterrupt`, `URLError`) |
| ex115 | Projeto — sistema de cadastro com persistência em arquivo | pacotes `lib.interface` (menu/validação) e `lib.arquivo` (leitura/escrita em `.txt`), combinando tudo que veio antes |
| `Scripys-python/` | Desafios soltos | primeiros testes de `input`/`print`, antes da numeração `exNNN` |

---

## 3. Cheat sheet de Python (referência rápida por tema)

### 3.1 Entrada e saída

```python
nome = input("Qual o seu nome? ")      # input() sempre retorna string
idade = int(input("Idade: "))          # conversão explícita é obrigatória
peso = float(input("Peso: "))
```

**Formatação de saída — três formas usadas no repositório:**
```python
print("Olá {}".format(nome))                 # .format()  → ex002 em diante
print(f"Olá {nome}")                         # f-string   → a partir de ex063
print("Olá %s" % nome)                       # não usado aqui, mas existe
```

Formatação numérica útil (muito usada nos exercícios de dinheiro/percentual):
```python
f"{valor:.2f}"     # 2 casas decimais           → "10.50"
f"{valor:>10.2f}"  # alinhado à direita, largura 10
f"{texto:<15}"     # alinhado à esquerda, largura 15
f"{texto:^30}"     # centralizado, largura 30
f"{'':=^40}"        # preenche com "=" centralizado (usado em títulos, ex044)
```

### 3.2 Métodos de string (muito cobrados em ex004, ex022–ex027)

```python
s.strip()          # remove espaços das pontas
s.upper() / s.lower()
s.isnumeric()      # só dígitos?
s.isalpha()        # só letras?
s.isspace()
s.istitle()        # "Está Assim"?
s.count("a")       # quantas vezes aparece
s.find("a")        # posição da 1ª ocorrência (-1 se não achar)
s.rfind("a")       # posição da última ocorrência
s.split()          # separa em lista de palavras
"".join(lista)     # junta lista em uma string
s[::-1]            # inverte a string (usado no palíndromo do ex053)
s[:5]              # fatiamento (slice) — pega os 5 primeiros caracteres
```

### 3.3 Módulo `math` (ex016–ex018)

```python
from math import trunc, sqrt, hypot
trunc(3.9)          # 3 → parte inteira, sem arredondar
sqrt(16)             # 4.0
hypot(3, 4)          # 5.0 → hipotenusa direto (equivalente a sqrt(a**2+b**2))

import math
math.radians(90)     # graus → radianos (necessário antes de sin/cos/tan)
math.sin(x); math.cos(x); math.tan(x)
```

### 3.4 Módulo `random` (ex019, ex020, ex028, ex058, ex068, ex088, ex091, ex100)

```python
from random import randint, choice, shuffle
randint(0, 10)        # inteiro aleatório entre 0 e 10 (inclusive)
choice(lista)         # escolhe 1 item aleatório da lista
shuffle(lista)        # embaralha a lista *no lugar* (não retorna nada)
```

### 3.5 Módulo `datetime` (ex032, ex039, ex041, ex054, ex092, ex101)

```python
from datetime import date, datetime
date.today().year          # ano atual
datetime.today().year      # também funciona
```

### 3.6 Condicionais (ex028–ex045)

```python
if condição:
    ...
elif outra_condição:
    ...
else:
    ...
```
- Use `and` / `or` para combinar condições (ex033, ex035, ex042).
- Cuidado com **precedência**: `a and b or c` pode não fazer o que parece — prefira parênteses quando tiver dúvida.
- Padrão "ano bissexto" (ex032):
  ```python
  bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
  ```

### 3.7 Laços `for` e `while`

```python
for c in range(inicio, fim, passo):   # fim é EXCLUSIVO
    ...

while condição:
    ...
    if condição_de_saida:
        break
```

Padrões recorrentes no repositório:
- **Contador/acumulador**: `cont = 0; soma = 0` fora do laço, `cont += 1; soma += valor` dentro.
- **Sentinela**: repetir "até digitar 999" (`while n != 999`) — ex064, ex066.
- **Confirmação S/N com validação**:
  ```python
  resp = ' '
  while resp not in "SN":
      resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if resp == "N":
      break
  ```
  Esse bloco aparece repetido em dezenas de exercícios (ex069, ex070, ex079, ex084, ex089, ex093...) — vale a pena guardar como "receita pronta".
- **Maior/menor em sequência de valores**: sempre inicializar `maior = menor = primeiro_valor` na primeira iteração (`if cont == 0`), e só comparar dali em diante (ex055, ex078).

### 3.8 Tuplas (ex072–ex077)

```python
t = (1, 2, 3, 4)
t[0]            # acesso por índice
t[0:5]          # slice
t[-4:]          # últimos 4 itens
sorted(t)       # retorna uma NOVA lista ordenada (tupla não tem .sort())
t.count(9)      # quantas vezes o valor 9 aparece
t.index(3)      # posição da primeira ocorrência de 3
```
Tuplas são imutáveis — por isso não existe `t.append()` ou `t.sort()`.

### 3.9 Listas (ex078–ex089)

```python
lista = []
lista.append(valor)      # adiciona no final
lista.insert(pos, valor) # adiciona em posição específica
lista.sort()             # ordena a própria lista (in place)
lista.clear()             # esvazia a lista
lista[:]                  # cópia da lista (shallow copy) — usado para "congelar" um registro (ex084, ex088)
for i, v in enumerate(lista):   # i = índice, v = valor
    ...
```
**Matriz (lista de listas)** — ex085 a ex087:
```python
matriz = [[0,0,0],[0,0,0],[0,0,0]]
matriz[linha][coluna] = valor
```

### 3.10 Dicionários (ex090–ex095)

```python
d = dict()
d['Nome'] = 'Ana'
d['Idade'] = 20
for chave, valor in d.items():
    print(chave, valor)

d.copy()          # cópia rasa — necessária ao guardar dicts numa lista em laço (ex094)
```
Combinações comuns:
- **Lista de dicionários**: cada `.append(d.copy())` dentro de um `while` cria um "cadastro" (ex094, ex095).
- **Dicionário com lista dentro**: `futebol['Gols'] = [gols de cada partida]` (ex093, ex095).
- **Ordenar dicionário por valor**: `sorted(d.items(), key=itemgetter(1), reverse=True)` (ex091) — requer `from operator import itemgetter`.

### 3.11 Funções (ex096–ex105)

```python
def nome_da_funcao(param1, param2=valor_padrao):
    """Docstring: explica o que a função faz."""
    ...
    return resultado
```
- **Parâmetro padrão**: `def ficha(nome="<desconhecido>", gols=0):` (ex103) — permite chamar a função sem passar todos os argumentos.
- **`*args`** (número variável de argumentos): `def maior(*num):` — dentro da função, `num` vira uma tupla (ex099, ex100 usa listas ao invés).
- **Argumento nomeado obrigando `=`**: `def notas(*n, sit=False):` — tudo depois de `*n` só pode ser passado como `nome=valor` (ex105).
- **Retornar um dicionário** é uma forma comum de "empacotar" vários resultados numa função só (ex105).
- **Docstring no padrão do curso**:
  ```python
  def factorial(num=0, show=False):
      '''
      -->Calcula o fatorial de um numero
      :param num: o valor a calcular
      :param show: mostra o cálculo passo a passo
      :return: o fatorial do número
      '''
  ```

### 3.12 Cores no terminal — ANSI escape codes (ex052, ex104, ex106)

```python
print("\033[0;31mtexto em vermelho\033[m")
```
Estrutura: `\033[<estilo>;<cor_texto>;<cor_fundo>m`. Termina sempre com `\033[m` para resetar a cor.
Exemplos usados no repositório:
```python
"\033[m"        # reset (sem cor)
"\033[0;30;41m" # texto preto, fundo vermelho
"\033[0;30;42m" # fundo verde
"\033[0;30;43m" # fundo amarelo
"\033[0;30;44m" # fundo azul
```

### 3.13 Tratamento de exceções (ex113, ex114)

```python
try:
    num = int(input(msg))
except (ValueError, TypeError):
    print('\033[0;31mErro! digite um número inteiro\033[m')
    continue           # volta pro início do while, pede de novo
except KeyboardInterrupt:
    print('Entrada de dados interrompida pelo usuário')
    return 0
else:
    return num          # só roda se NENHUMA exceção ocorreu
finally:
    pass                # sempre roda, tenha dado erro ou não (não usado no ex113)
```

Papel de cada bloco:
- **`try`**: código que pode falhar.
- **`except X`**: só captura o tipo de erro `X` (pode listar vários tipos entre parênteses). Evite `except:` genérico — ele esconde bugs que nada têm a ver com o que você queria tratar (foi o que causou os erros do `ex115` antigo, ver seção 5).
- **`else`**: roda **só se não houve exceção** — é o lugar certo para o "caminho feliz" (ex.: fechar o arquivo, retornar o valor).
- **`finally`**: roda **sempre**, com ou sem erro — bom para liberar recursos (fechar arquivo/conexão), mas cuidado: se a variável só existe quando o `try` deu certo, usar `a.close()` num `finally` pode gerar `NameError` quando o `try` falha (ver seção 5).

**Erros específicos de arquivo/rede usados no repositório:**
```python
except FileNotFoundError:   # arquivo não existe (ex. arquivoExiste, ex115)
except urllib.error.URLError:  # falha de conexão/rede (ex114)
```

### 3.14 Módulos e pacotes (ex107–ex112)

**Módulo simples** (ex107–ex110): um arquivo `moeda.py` com funções, importado de outro arquivo na mesma pasta:
```python
# moeda.py
def dobro(num):
    return num * 2

# teste.py (na mesma pasta ex107/)
from ex107 import moeda
moeda.dobro(10)
```

**Pacote** (ex111–ex112): uma pasta vira um "pacote" quando tem um arquivo `__init__.py` dentro — mesmo vazio. Isso permite organizar módulos em subpastas:
```
ex112/
├── teste.py
└── utilidadesCeV/
    ├── __init__.py
    ├── moeda/
    │   └── __init__.py   (funções de moeda ficam aqui dentro)
    └── dados/
        └── __init__.py   (funções de leitura/validação de dados)
```
```python
from ex112.utilidadesCeV import moeda, dados
dados.leiaDinheiro("Digite um valor: ")
moeda.resumo(p, 20, 40)
```
Esse é o padrão mais avançado do repositório: separar "utilidades" reaproveitáveis em pacotes.

### 3.15 Estudo de caso: `ex115` — projeto completo (menu + validação + arquivo)

`ex115` é o exercício mais avançado do repositório: um sisteminha de cadastro de pessoas com menu, validação de entrada e persistência em arquivo `.txt`, organizado em dois pacotes:

```
ex115/
├── sistema.py                     → programa principal (o "main")
└── lib/
    ├── interface/__init__.py      → menu, cabecalho, linha, leiaInt
    └── arquivo/__init__.py        → arquivoExiste, criarArquivo, lerArquivo, criarCadastro
```

Repare que `lib/interface` e `lib/arquivo` são **pacotes** (pastas com `__init__.py`), não módulos soltos (`.py` avulso) — por isso `sistema.py` importa assim:
```python
from ex115.lib.interface import *
from ex115.lib.arquivo import *
```

**Fluxo do `sistema.py`:**
```python
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)          # só cria o arquivo vazio, não grava registro nenhum

while True:
    resposta = menu([...])      # mostra o menu e já valida a opção digitada
    if resposta == 1:
        lerArquivo(arq)          # lê e mostra os cadastros
    elif resposta == 2:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        criarCadastro(arq, nome, idade)   # acrescenta uma linha "nome;idade"
    elif resposta == 3:
        break
```

**Formato de armazenamento:** cada linha do `cursoemvideo.txt` é `nome;idade\n` — por isso `lerArquivo` precisa fazer `linha.strip().split(';')` para separar os dois campos antes de exibir.

**Por que `try/except/else/finally` junto (e não só `try/except`)?** Nesse projeto o padrão usado é:
```python
try:
    a = open(arq, 'at')
except:
    print('Houve um erro na abertura do arquivo')
else:
    try:
        a.write(f'{nome};{idade}\n')
    except:
        print('Houve um erro na hora de escrever os dados')
    else:
        print('Novo cadastro adicionado com sucesso')
    finally:
        a.close()
```
A escrita fica **dentro do `else`** da abertura — assim ela só é tentada quando o arquivo abriu de verdade. E o `a.close()` fica no `finally` **de dentro**, que só existe se o `else` de fora rodou — ou seja, `a` sempre existe ali dentro. Esse é o padrão seguro para "abrir → usar → sempre fechar" sem arriscar usar uma variável que nunca chegou a existir.

Esse exercício é um bom lugar para revisar quando precisar montar do zero um programa com menu + cadastro + arquivo — é basicamente o "resumo" de tudo que os exercícios anteriores ensinaram separadamente.

---

## 4. Padrões de código recorrentes (vale copiar e colar)

**Validar número inteiro digitado (ex104):**
```python
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        print("Erro! Digite um número inteiro")
```

**Validar sexo M/F (repetido em vários exercícios):**
```python
sexo = ''
while sexo not in 'MF':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
```

**Formatar valor em moeda (ex108–ex112):**
```python
def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
```

**Contagem regressiva com pausa (ex046, ex098):**
```python
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
```

---

## 5. Pontos de atenção observados no código (para não repetir os mesmos deslizes)

Estes são detalhes reais encontrados nos exercícios — bons para revisar quando for reler seu próprio código:

- **`ex036.py`**: `.format(Casa, Anos, end='')` — o parâmetro `end=''` não tem efeito dentro de `.format()`; ele é argumento de `print()`, não de `.format()`. Se a intenção era não pular linha, o `end=''` deveria estar em `print(..., end='')`.
- **`Scripys-python/desafio03.py`**: `soma1 + soma2` concatena strings (já que `input()` sempre retorna string) em vez de somar números — para somar de fato, seria necessário `int(input(...))`.
- **`ex093.py`**: o laço usa `range(0, partidas + 1)`, o que registra **uma partida a mais** que o informado (ex.: 3 partidas pede 4 valores de gols). O padrão correto normalmente usado no resto do repositório é `range(0, partidas)`.
- **`ex040.py`**: a condição `elif m >= 5.0 or m <= 6.0` é sempre verdadeira (todo número é `<= 6.0` ou `>= 5.0`) — na prática isso nunca deixa cair no `else`. O certo seria `elif 5.0 <= m < 7.0` (usar `and`, não `or`).
- Vários exercícios (`ex056`, `ex094`) somam idades de "5 pessoas" mas dividem por um número fixo diferente (ex.: `ex056` divide por 4) — vale conferir se o divisor bate com a quantidade real de iterações do laço.
- **`ex115`** passou por rodadas de correção (histórico útil para não repetir): `leiaInt` retornava dentro do próprio `while` (saía com `0` no primeiro erro); `lerArquivo` não separava `nome;idade` com `.split(';')`; `a.close()`/`a.write()` estavam em blocos `finally` que rodavam mesmo quando o `open()` falhava, gerando `NameError`; e o `sistema.py` chamava `criarCadastro(arq)` em vez de `criarArquivo(arq)` ao inicializar, gravando um registro fantasma `"desconhecido;0"`. A versão atual (seção 3.15) já está corrigida — regra geral: **o que só deve rodar quando o `try` deu certo vai no `else`, não no `finally`**.

---

## 6. Índice completo por número de exercício

| Exercício | Tema em uma linha |
|---|---|
| ex001 | `print` básico |
| ex002 | `input` + `.format()` |
| ex003 | soma de dois números |
| ex004 | métodos de verificação de string (`isnumeric`, `isalpha`...) |
| ex005 | sucessor e antecessor |
| ex006 | dobro, triplo, raiz quadrada |
| ex007 | média de duas notas |
| ex008 | conversão de metros para cm/mm |
| ex009 | tabuada de um número |
| ex010 | conversão R$ → dólar |
| ex011 | cálculo de área e tinta necessária |
| ex012 | desconto de 5% |
| ex013 | aumento salarial de 15% |
| ex014 | Celsius → Fahrenheit |
| ex015 | cálculo de aluguel de carro (km + diária) |
| ex016 | `math.trunc` |
| ex017 | hipotenusa (`sqrt`/`hypot`) |
| ex018 | seno, cosseno, tangente |
| ex019 | `random.choice` — sorteio de aluno |
| ex020 | `random.shuffle` — ordem de apresentação |
| ex021 | tocar áudio com `pygame` |
| ex022 | maiúsculo/minúsculo/contagem de letras do nome |
| ex023 | separar unidade/dezena/centena/milhar |
| ex024 | verificar se cidade começa com "Santo" |
| ex025 | verificar se nome contém "Silva" |
| ex026 | contar ocorrências da letra A numa frase |
| ex027 | primeiro e último nome |
| ex028 | jogo de adivinhação simples (`if/else`) |
| ex029 | multa por excesso de velocidade |
| ex030 | par ou ímpar |
| ex031 | preço de passagem por distância |
| ex032 | ano bissexto |
| ex033 | maior/menor entre 3 números |
| ex034 | aumento salarial condicional (10%/15%) |
| ex035 | verificar se 3 lados formam triângulo |
| ex036 | simulação de financiamento de casa |
| ex037 | conversão para binário/octal/hexadecimal |
| ex038 | comparar dois valores |
| ex039 | verificar se pode se alistar |
| ex040 | aprovação por média (contém bug, ver seção 5) |
| ex041 | categoria de atleta por idade |
| ex042 | tipo de triângulo (equilátero/isósceles/escaleno) |
| ex043 | cálculo de IMC |
| ex044 | loja com formas de pagamento e desconto |
| ex045 | pedra-papel-tesoura contra o computador |
| ex046 | contagem regressiva com `sleep` |
| ex047 | números pares de 2 a 50 |
| ex048 | soma de múltiplos de 3 entre 1 e 500 (ímpares) |
| ex049 | tabuada com `for` |
| ex050 | soma de valores pares digitados |
| ex051 | progressão aritmética (PA) com `for` |
| ex052 | verificar se número é primo (com cores no terminal) |
| ex053 | verificar palíndromo |
| ex054 | contar maiores/menores de idade |
| ex055 | maior e menor peso de 5 pessoas |
| ex056 | estatísticas de grupo (idade média, homem mais velho, mulheres <20) |
| ex057 | validar entrada de sexo M/F |
| ex058 | jogo de adivinhação com "quente/frio" |
| ex059 | calculadora com menu (`while` + opções) |
| ex060 | fatorial (duas soluções: `while` e `for`) |
| ex061 | gerador de PA (10 termos) |
| ex062 | gerador de PA com quantidade customizável |
| ex063 | sequência de Fibonacci |
| ex064 | soma de valores até digitar 999 (sentinela) |
| ex065 | maior, menor e média de valores digitados |
| ex066 | soma de valores com sentinela (versão com `break`) |
| ex067 | tabuada em loop até valor negativo |
| ex068 | jogo par ou ímpar contra o computador |
| ex069 | estatísticas de cadastro (idade, sexo) em loop |
| ex070 | produto mais barato e mais caro numa lista de compras |
| ex071 | "Banco CEV" — saque dividido em cédulas |
| ex072 | número por extenso (0 a 20) usando tupla |
| ex073 | tupla de times do Brasileirão, slices e `sorted` |
| ex074 | maior/menor de 5 números sorteados (tupla) |
| ex075 | análise de tupla de 4 valores digitados |
| ex076 | lista de produtos com preços formatados |
| ex077 | vogais de uma lista de palavras |
| ex078 | maior/menor valor com posição (`enumerate`) |
| ex079 | lista sem valores duplicados, ordenada |
| ex080 | inserir valor em lista já ordenada |
| ex081 | (lista — ver arquivo para detalhes específicos) |
| ex082 | separar números pares e ímpares em listas |
| ex083 | validar parênteses de uma expressão (pilha) |
| ex084 | maior/menor peso com nome (lista de listas) |
| ex085 | separar pares/ímpares usando lista de listas |
| ex086 | preencher e exibir matriz 3x3 |
| ex087 | soma de pares, soma de coluna e maior valor de linha numa matriz |
| ex088 | sorteio de jogos da loteria (números sem repetição) |
| ex089 | boletim de alunos com consulta por índice |
| ex090 | dicionário simples de aluno + situação |
| ex091 | ranking de dado por jogador (`sorted` + `itemgetter`) |
| ex092 | cadastro com aposentadoria (dicionário condicional) |
| ex093 | estatísticas de gols de um jogador (dicionário + lista) |
| ex094 | cadastro de várias pessoas (lista de dicionários) |
| ex095 | cadastro de vários jogadores com consulta detalhada |
| ex096 | função simples — cálculo de área |
| ex097 | função que "emoldura" um texto |
| ex098 | função de contagem com passo customizável |
| ex099 | função com `*args` para achar o maior valor |
| ex100 | funções que sorteiam e somam números pares |
| ex101 | função que retorna situação de voto por idade |
| ex102 | função de fatorial com docstring e parâmetro `show` |
| ex103 | função com parâmetros padrão (ficha de jogador) |
| ex104 | função de validação de entrada inteira |
| ex105 | função com `*args` e argumento nomeado (`sit=`) retornando dicionário |
| ex106 | sistema de ajuda com cores ANSI + `help()` |
| ex107 | módulo `moeda.py` — operações básicas |
| ex108 | módulo `moeda.py` — adiciona formatação em R$ |
| ex109 | módulo `moeda.py` — parâmetro `formato` em cada função |
| ex110 | módulo `moeda.py` — adiciona função `resumo()` |
| ex111 | pacote `utilidadesCeV` com subpacote `moeda` |
| ex112 | pacote `utilidadesCeV` com subpacotes `moeda` e `dados` |
| ex113 | `leiaInt`/`leiaFloat` com `try/except/else`, tratando `ValueError` e `KeyboardInterrupt` |
| ex114 | requisição HTTP com `urllib.request`, tratando `URLError` |
| ex115 | projeto completo: sistema de cadastro com menu, validação e arquivo (`lib.interface` + `lib.arquivo`) — ver seção 3.15 |
| `Scripys-python/Teste01.py` | teste de `input` múltiplo |
| `Scripys-python/desafio01.py` | boas-vindas simples |
| `Scripys-python/desafio02.py` | ler data de nascimento |
| `Scripys-python/desafio03.py` | soma de dois números (contém bug, ver seção 5) |

---

## 7. Como usar esta documentação no dia a dia

- **Esqueceu como formatar dinheiro?** → seção 3.14 / 3.1.
- **Esqueceu como tratar erros com `try/except`?** → seção 3.13.
- **Quer ver um projeto completo juntando tudo (menu + validação + arquivo)?** → seção 3.15.
- **Esqueceu como validar uma entrada (S/N, número, sexo)?** → seção 4.
- **Esqueceu como funciona `*args` ou parâmetro padrão?** → seção 3.11.
- **Não lembra em qual exercício viu determinado tema?** → seção 6 (índice completo).
- **Quer relembrar um erro que já cometeu?** → seção 5.

Sempre que fizer um exercício novo, considere voltar aqui e adicionar uma linha na tabela do índice (seção 6) e, se aprender um padrão novo, uma entrada na seção 4.

## Agradecimentos

Repositório construído acompanhando o curso de Python do **Guanabara** (Curso em Vídeo).
Obrigado, Guanabara! 🙏