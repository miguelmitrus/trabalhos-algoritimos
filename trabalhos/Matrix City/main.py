cidade = [
    [1, 0, 2, 0, 1],
    [0, 9, 2, 1, 3],
    [1, 0, 1, 9, 2],
    [9, 3, 0, 2, 1],
    [0, 1, 2, 0, 9]
]

#missão 1

casas = 0
hospitais = 0
geradores = 0
destruidas = 0

print("=== MAPA DE MatrixCity ===")

for i in range(len(cidade)):
    for j in range(len(cidade[i])):

        print(cidade[i][j], end=" ")

        if cidade[i][j] == 1:
            casas += 1

        elif cidade[i][j] == 2:
            hospitais += 1

        elif cidade[i][j] == 3:
            geradores += 1

        elif cidade[i][j] == 9:
            destruidas += 1

    print()

print("\n=== RELATÓRIO ===")
print("Casas:", casas)
print("Hospitais:", hospitais)
print("Geradores:", geradores)
print("Áreas destruídas:", destruidas)

#missão 2

print("\n=== HOSPITAIS EM PERIGO ===")

for i in range(len(cidade)):
    for j in range(len(cidade[i])):

        if cidade[i][j] == 2:

            perigo = False

            #cima
            if i > 0:
                if cidade[i - 1][j] == 9:
                    perigo = True

            #baixo
            if i < len(cidade) - 1:
                if cidade[i + 1][j] == 9:
                    perigo = True

            #esquerda
            if j > 0:
                if cidade[i][j - 1] == 9:
                    perigo = True

            #direita
            if j < len(cidade[i]) - 1:
                if cidade[i][j + 1] == 9:
                    perigo = True

            if perigo:
                print(f"Hospital em ({i},{j}): EM PERIGO!")

            else:
                print(f"Hospital em ({i},{j}): SEGURO")

#missão 3

print("\n=== ALCANCE DOS GERADORES ===")

total_atendidos = 0

for i in range(len(cidade)):

    possui_gerador = False

    for j in range(len(cidade[i])):

        if cidade[i][j] == 3:
            possui_gerador = True

    if possui_gerador:

        encontrados = []

        for j in range(len(cidade[i])):

            if cidade[i][j] == 2:
                encontrados.append(f"({i},{j})")
                total_atendidos += 1

        if len(encontrados) == 0:
            print(f"Gerador na linha {i} -> Hospitais atendidos: nenhum")

        else:
            print(
                f"Gerador na linha {i} -> Hospitais atendidos:",
                ", ".join(encontrados)
            )

print("Total de hospitais com energia:", total_atendidos)

#missão 4 

print("\n=== ROTAS DE EVACUAÇÃO ===")

existe_segura = False

for i in range(len(cidade)):

    segura = True

    for j in range(len(cidade[i])):

        if cidade[i][j] == 9:
            segura = False

    if segura:
        existe_segura = True
        print(f"Linha {i}: SEGURA ✓")

    else:
        print(f"Linha {i}: BLOQUEADA ✗")

if not existe_segura:
    print("\nALERTA: Nenhuma rota segura encontrada!")