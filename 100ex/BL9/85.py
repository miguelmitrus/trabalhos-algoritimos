matriz = []

for i in range(4):
    linha = []

    for j in range(4):
        linha.append(int(input(f"Digite [{i}][{j}]: ")))

    matriz.append(linha)

for i in range(4):

    soma = 0

    for j in range(4):
        soma += matriz[i][j]

    print(f"Soma da linha {i}:", soma)