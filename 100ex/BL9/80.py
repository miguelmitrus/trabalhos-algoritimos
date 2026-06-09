matriz = []
soma = 0

for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
        soma += valor

    matriz.append(linha)

print("Soma dos elementos:", soma)