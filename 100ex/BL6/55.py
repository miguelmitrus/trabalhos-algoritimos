numero = int(input("Digite um número positivo: "))

soma = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        soma += i

print("Soma dos divisores:", soma)