matriz = []

for i in range(3):
    linha = []

    for j in range(4):
        linha.append(int(input(f"Digite [{i}][{j}]: ")))

    matriz.append(linha)

transposta = []

for j in range(4):

    linha = []

    for i in range(3):
        linha.append(matriz[i][j])

    transposta.append(linha)

print("Matriz transposta:")

for linha in transposta:
    print(linha)