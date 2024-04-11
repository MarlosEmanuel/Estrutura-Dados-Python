# Sets

"""
    Um set é uma coleção que não possui objetos
repetidos, usamos sets para representar conjuntos
matemáticos ou eliminar itens duplicados de um interável

"""

# Exemplo

set([1,2,3,1,3,4]) # {1,2,3,4}

set("abacaxi") # {"b","a","c","x","i"}

set("palio","gol","celta","palio") # {"gol","celta","palio"}


# Acessando dados

"""
    Conjuntos em Python não suportam indexação e nem
fatiamento, caso queira acessar os seus valores é necessário
converter o conjunto para lista.

"""

# Exemplo

numeros = {1,2,3,2}

numeros = list(numeros)

numeros[0] # 1 

# iterar conjuntos

carros = {"gol","celta","palio"}

for carro in carros:
    print(carro)


# Metodos da classe set

#{}.union
# unir conjuntos
conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b) # {1,2,3,4}


# {}.intersection
# valores que há no dois conjuntos

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) # {2,3}

# {}.difference
# Subtração de um conjuntos menos o outro

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}


# {}.symmetric_difference
# Somente os elementos que não está ne interceção

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) # {1,4}


# {}.issubset
# usado para saber se conjuntos é subconjunto do outro

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # false


# {}.issuperset
# é o contrario
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # Verdadeiro

# {}.isdisjoint
# Operação de conjunto dijunto

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False


# {}.add
# Adiciona elementos, ele não deixa adicionar elementos iguais

sorteio = {1,23}

sorteio.add(25) # {1,23,25}
sorteio.add(42) # {1,23,25,42}
sorteio.add(25) # {1,23,25,42}


# {}.clear
# Limpa o set

sorteio = {1,23}

sorteio # {1,23}
sorteio.clear()
sorteio # {}


# {}.copy

sorteio = {1,23}

sorteio # {1,23}
sorteio.copy()
sorteio #{1,23}


#{}.discard
# Discarta valores

numeros = {1,2,3,1,2,4,5,6,7,8,9,0}

numeros.discard(1)
numeros.discard(45) # Ignora

numeros # {2,3,4,5,6,7,8,9,0}


# {}.pop
# Metodo de pilha

numeros = {0,1,2,3,1,2,4,5,6,7,8,9}

numeros.pop() # 0
numeros.pop() # 1

numeros # {2,3,1,2,4,5,6,7,8,9}


# {}.remove
# remove um valor

numeros = {1,2,3,1,2,4,5,6,7,8,9,0}

numeros.discard(1) 
numeros.discard(45) # Ignora

numeros # {2,3,1,2,4,5,6,7,8,9,0}


# Len
# Mostra o tamanho do set

numeros = {1,2,3,1,2,4,5,6,7,8,9,0}
len (numeros) # 10


# in
# para saber o objeto esta no conjunto

numeros = {1,2,3,1,2,4,5,6,7,8,9,0}

1 in numeros # True
10 in numeros # False