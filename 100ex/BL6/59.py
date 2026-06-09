numero = int(input("Digite um número: "))

soma = 0

for i in range(1, numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print("É um número perfeito.")
else:
    print("Não é um número perfeito.")