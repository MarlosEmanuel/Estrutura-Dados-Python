"""
    Tuplas são estrutura de dados muito parecidas com as listas
a principal diferença é que as tuplas são imutaveis enquanto listas
são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores
separados por vírgula de parenteses.

"""

# Exemplo:

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)


# Acessando valores da tupla

frutas = ("maçã","laranja","uva","pera",)

frutas[0] # maçã
frutas[2] # uva

#indices negativos

frutas[-1] # pera
frutas[-3] # laranja

# Matriz de Tuplas

matriz = (
    (1,"a",2)
    ("b",3,4)
    (6,5,"c")
)

matriz[0] # (1,"a",2)
matriz [0][0] # 1
matriz [0][-1] # 2
matriz [-1][-1] # "c"

# percorrendo tupla

carros = ("gol","celta","palio",)

for carros in carros:
    print(carros)


# Metodos da classe tuple


# ().count
# funcao mostra quantos determinados objetos tem na tupla

cores = ("vermelho","azul","verde","azul")

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# ().index

linguagens = ("python","js","c","java","csharp",)

linguagens.index("java") # 3
linguagens.index("Python") # 0

#len
# Conta quantos elementos tem em uma tupla

linguagens = ("python","js","c","java","csharp",)
len(linguagens) # 5



