matriz1 = []
matriz2 = []
resultado = []

print("Primeira matriz")

for i in range(2):
    linha = []

    for j in range(2):
        linha.append(int(input(f"Digite [{i}][{j}]: ")))

    matriz1.append(linha)

print("Segunda matriz")

for i in range(2):
    linha = []

    for j in range(2):
        linha.append(int(input(f"Digite [{i}][{j}]: ")))

    matriz2.append(linha)

for i in range(2):
    linha = []

    for j in range(2):
        linha.append(matriz1[i][j] + matriz2[i][j])

    resultado.append(linha)

print("Matriz soma:")

for linha in resultado:
    print(linha)