print("Olá mundo")

print(7+4)
print("7 + 4")
print("7" + "4") # Concatenação de string

# Comentário de 1 linha

'''
    Comentários de multiplas linhas
    Autor: Temitope Kuku
'''

#Variáveis

Nome = "Temitope" #string
Idade = 18 #inteiro
Peso = 83.5 # float
print(Nome, Idade, Peso)
print("Olá {}".format(Nome))

# Input - Simulação de forms no CMD

Nome = input("Digite o seu nome: ")
print(Nome)
Idade = int(input("Digite a sua idade: "))
Peso = float(input("Digite o seu peso: "))

print(Nome,Idade,Peso)
print(Idade + 1)

Ano_Nascimento = 2008
Ano_Atual = 2026

Idade = Ano_Atual - Ano_Nascimento

print("Sua idade é: {}".format(Idade))