#FUNÇÃO SEM RETORNO E SEM PARAMÊTRO
def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while i'm alive")

print_lyrics()

#FUNÇÃO SEM RETORNO E COM PARAMÊTRO
def boas_vindas(nome):
    print(f"Olá {nome}, sejá bem vindo!")

nome_digitado = input("Digite o seu nome: ")
boas_vindas(nome_digitado)

#FUNÇÃO COM RETORNO E COM PARAMETRO
def soma(num_a,num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(17,22)
print(resultado_soma)