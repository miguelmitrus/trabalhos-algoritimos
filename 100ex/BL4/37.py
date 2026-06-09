preco = float(input("Digite o preço do produto: "))

print("1 - À vista")
print("2 - Em 2 vezes")
print("3 - Em 3 vezes")

opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    total = preco * 0.90
    print("Valor final:", total)

elif opcao == 2:
    print("Valor final:", preco)

elif opcao == 3:
    total = preco * 1.10
    print("Valor final:", total)

else:
    print("Opção inválida.")