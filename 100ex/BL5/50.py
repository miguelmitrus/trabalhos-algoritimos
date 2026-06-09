opcao = 0

while opcao != 5:

    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao >= 1 and opcao <= 4:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", num1 + num2)

        elif opcao == 2:
            print("Resultado:", num1 - num2)

        elif opcao == 3:
            print("Resultado:", num1 * num2)

        elif opcao == 4:
            print("Resultado:", num1 / num2)

    elif opcao == 5:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")