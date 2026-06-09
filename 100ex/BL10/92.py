def soma_diagonal(matriz):

    soma = 0

    for i in range(len(matriz)):
        soma += matriz[i][i]

    return soma


matriz = []

for i in range(3):

    linha = []

    for j in range(3):
        linha.append(int(input(f"Digite [{i}][{j}]: ")))

    matriz.append(linha)

print("Soma da diagonal:", soma_diagonal(matriz))