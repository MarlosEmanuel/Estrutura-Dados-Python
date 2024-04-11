#Metodos:

# [].append
# função para adicionar um objeto a uma lista

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]


# [].clear
# função para limpar a lista

lista.clear()

print(lista) # []

# [].copy
# função para copiar uma lista

lista = [1, "python" , [40, 30, 20]]

l2 = lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

# lista na pos 0 será 1, e l2 na posicao 0 será 2
# Objetos diferentes


# [].count
# função conta quantas vezes um objeto aparece na sua lista

cores  = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") #1
cores.count("azul") #2
cores.count("verde") #1

# [].extend
# função para juntar duas listas. OBS: Ele não elimina objetos iguais

linguagens = ["Python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens) #["Python", "js", "java","csharp"]

# [].index
# ele retorna qual a posição do objeto na sua lista, passando como parametro um objeto
# Obs: ele retorna apenas a primeira vez que o objeto aparece na lista

linguagens.index ("java") # 3
linguagens.index("python") # 0

# [].pop
# estrutura de pilha, sai o ultimo objeto da lista

linguagens.pop() # cshap
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python


# [].remove

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) # ["Python", "js", "java", "csharp"]


# [].reverse
# função para reverter uma lista

linguagens = ["Python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) # ["csharp", "java", "c", "js", "python"]


# [].sort

# Ordena a lista de forma alfabetica
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

# Ordena de forma alfabetica e depois reverte
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "c"]

# Ordena de forma crescente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(kay=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

# Ordena de forma crescente depois reverte
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]

# retorna o tamanho da lista
linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens) #5


# Sorted
# mesma coisa do sort

linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x))


linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x), reverse=True)