matriz = []
pares = 0

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))

        if valor % 2 == 0:
            pares += 1

        linha.append(valor)

    matriz.append(linha)

print("Quantidade de números pares:", pares)