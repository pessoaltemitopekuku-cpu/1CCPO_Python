# 0 --- Sair do programa
# 1 --- Entrar no programa
# --- erro !!

escolha_usuario = 4

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro")