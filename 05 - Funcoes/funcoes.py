# Funcoes

"""

    Função é um bloco de código identificado por um nome e pode receber uma lista e parâmetros, esses parâmetros podem ou não ter valores
padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer
que estamos programando de maneira estruturada.

"""

# Exemplo

def exibir_mensagem():
    print("Hello Word!")

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Marlos")
exibir_mensagem_3()
exibir_mensagem_3(nome="Marlos")



# Retornando Valores

"""

Para retornar um valor, utilizamos a palavra reservada return.
Toda função em python retorna None por padrão. 
Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

"""

# Exemplo

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor,sucessor

calcular_total([10, 20, 34]) #64
retorna_antecessor_e_sucessor(10) # (9,11)


# Argumento Nomeado

"""
Funções também podem ser chamadas usando argumentos nomeados a forma chave:valor

"""

def salvar_carro(marca,modelo,ano,placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca/{modelo}/{ano}/{placa}}")

salvar_carro("Fiat","Palio",1999,"ABC-1234")
salvar_carro(nome="Fiat",modelo="Palio",ano=1999,placa="ABC-1234")
salvar_carro(**{"marca":"fiat","modelo":"Palio","ano":1999,"placa":"ABC-1234"})

# Carro inserio com sucesso! fiat/palio/1999/ABC-1234


# Args e Kwargs

"""
    Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos(*args e **kwargs),
o método recebe os valores como tupla e dicionario respectivamente.

"""

# Exemplo

def exibir_poema(data_extenso,*args,**kwargs):
    texto = "\n".joins(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave,valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen Of Python", "Beautiful is better than ugly.", autor = "Tim Peters", ano = 1999)