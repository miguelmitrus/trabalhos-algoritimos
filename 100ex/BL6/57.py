senha_correta = "python123"

tentativas = 0

while tentativas < 3:

    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Login realizado com sucesso.")
        break

    else:
        tentativas += 1
        print("Senha incorreta.")

if tentativas == 3:
    print("Número máximo de tentativas atingido.")