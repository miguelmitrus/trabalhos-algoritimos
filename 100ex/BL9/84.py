matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        linha.append(int(input(f"Digite [{i}][{j}]: ")))

    matriz.append(linha)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(3):
    for j in range(3):

        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print("Maior valor:", maior)
print("Linha:", linha_maior)
print("Coluna:", coluna_maior)