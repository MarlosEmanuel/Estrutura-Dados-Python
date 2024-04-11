# Criando um dicionário

"""
    Um dicionário é um conjunto não ordenado de pares
chave:valor, onde as chaves são únicas em uma dada instância
o dicionário. Dicionários são delimitados por chaves: {}, e
contém uma lista de pares chave:valor separadad por vírgulas.

"""

# Exemplo

pessoa = {"nome":"Marlos","idade":20}

pessoa = dict(nome="Marlos",idade=20)

pessoa["telefone"] = "3333-1234" # {"nome": "Marlos", "idade":28, "telefone": 3333-1234}


# Adicionando um valor a um dicionario

dados = {"nome":"Marlos","idade":20,"telefone":"3333-1234"}

dados ["nome"] # "Marlos"
dados ["idade"] # 28
dados ["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados # {"nome":"Maria", "idade":18, "telefone":"9988-1781"}


# Dicionarios aninhados

"""

Dicionarios podem armazenas qualquer tipo de objeto python
como valor, esde que a chave para esse valor seja um objeto
imutável(strings e números)

"""

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie","telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine","telefone":"3333-7766"},

}

contatos["giovanna@gmail.com"]["telefone"] # "3443-2121"


# Iterar dicionários

for chave in contatos:
    print(chave,contatos[chave])

for chave, valor in contatos.items():
    print(chave,valor)



# Metodos da classe dic


# {}.clear
# Limpa o dicionario

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie","telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine","telefone":"3333-7766"},

}

contatos.clear()
contatos # {}


# {}.copy

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"}

}

copia = contatos.copy()

copia["guilherme@gmail.com"] = {"nome":"gui"}

contatos["guilherme@gmail.com"] # {"nome":"guilherme", "telefone":"3333-2221"}
copia["guilherme@gmail.com"] # {"nome":"Gui"}


# {}.fromkeys
# Cria chaves, em duas situações

# Situação criar somente a chave sem valor
# Situação criar um conjunto de chave e colocar um valor padrao dela

dict.fromkeys(["nome","telefone"]) # {"nome": None, "telefone": None}
dict.fromkeys(["nome","telefone"],"vazio") # {"nome": "vazio", "telefone" : "vazio"}


# {}.get

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"}

}

contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave",{}) #{}
contatos.get("guilherme@gmail.com",{}) # {"guilherme@gmail.com": {"nome": "guilherme", "telefone":"3333-2221"}


#{}.keys
# retorna as chaves do dicionario


contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"}

}

contatos.keys() # dict_keys(['guilherme@gmail.com'])



# {}.pop
# metodo pilha

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"}

}

contatos.pop("guilherme@gmail.com") # {'nome':'guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme.com",{}) # {}



# {}.popitem
# Nao informa a chave, e vai retirando os itens igual a pilha

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"}

}

contatos.popitem() #('guilherme@gmail.com',{'nome':'guilherme','telefone':'3333-2221'})
contatos.popitem() #KeyError]



# {}.setdefault
# Se o atributo não existir no dicionario, ele adiciona com oque eu quero


contato = {"nome":"Guilherme","telefone":3333-2221}

contatos.setdefault("idade",28) # 28

print(contato) # {'nome': 'Guilherme', 'telefone':'3333-2221','idade':28}



# {}.update

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"}

}

contatos.update({"guilherme@gmail.com":{"nome":"Gui"}})
contatos # {'guilherme@gmail.com':{'nome':'Gui'}}

contatos.update({"giovanna@gmail.com":{"nome":"Giovanna","telefone":"3322--8181"}}) # adiciona no dicionario



# {}.values

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie","telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine","telefone":"3333-7766"},

}

contatos.values() # retorna somente os valores



# in
#saber se uma chave existe ou nao


contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie","telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine","telefone":"3333-7766"},

}

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False


# Del
# remove o objeto que eu desejo

contatos = {

    "guilherme@gmail.com":{"nome":"Guilherme","telefone":"333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna","telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie","telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine","telefone":"3333-7766"},

}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos ["chappie@gmail.com"]

