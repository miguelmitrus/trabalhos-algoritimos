soma = 0
quantidade = 0

while True:

    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        soma += numero
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print("Média dos pares:", media)
else:
    print("Nenhum número par foi informado.")