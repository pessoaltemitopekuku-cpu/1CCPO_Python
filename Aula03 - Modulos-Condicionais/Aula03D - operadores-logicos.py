#LÓGICA E (AND)

verifica_email = False
verifica_senha = True

login = verifica_senha and verifica_email
print(login)

if not login:
    print("Loga certo aí cara")