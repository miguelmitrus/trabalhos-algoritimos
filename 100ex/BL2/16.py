preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_final = preco - (preco * desconto / 100)

print("Valor final:", valor_final)