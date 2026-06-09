from utils import *

produtos = [
    "Produto A",
    "Produto B",
    "Produto C",
    "Produto D"
]

dias = [
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
    "Domingo"
]

vendas = [
    [45, 38, 52, 41, 60, 55, 21],
    [30, 42, 35, 48, 39, 55, 29],
    [28, 35, 40, 33, 45, 38, 22],
    [46, 47, 35, 40, 27, 53, 23]
]

print("===== RELATÓRIO DE VENDAS — SEMANA =====\n")

print("--- Por produto ---")

totais_produtos = []

total_geral = 0

for i in range(len(produtos)):

    total = calcular_total(vendas[i])
    media = calcular_media(vendas[i])

    totais_produtos.append(total)
    total_geral += total

for i in range(len(produtos)):

    total = totais_produtos[i]
    media = calcular_media(vendas[i])

    percentual = calcular_percentual(total, total_geral)

    print(
        formatar_linha(
            produtos[i],
            total,
            media,
            percentual
        )
    )

print("\n--- Por dia ---")

totais_dias = []

for j in range(len(dias)):

    lista = []

    for i in range(len(produtos)):
        lista.append(vendas[i][j])

    total = calcular_total(lista)
    media = calcular_media(lista)

    totais_dias.append(total)

    print(
        formatar_linha(
            dias[j],
            total,
            media
        )
    )

print("\n-----------------------------------------")

melhor_produto = encontrar_maior(
    totais_produtos,
    produtos
)

pior_produto = encontrar_menor(
    totais_produtos,
    produtos
)

melhor_dia = encontrar_maior(
    totais_dias,
    dias
)

pior_dia = encontrar_menor(
    totais_dias,
    dias
)

print(
    "Melhor produto :",
    melhor_produto[0],
    f"({melhor_produto[1]} un)"
)

print(
    "Pior produto   :",
    pior_produto[0],
    f"({pior_produto[1]} un)"
)

print(
    "Melhor dia     :",
    melhor_dia[0],
    f"({melhor_dia[1]} un)"
)

print(
    "Pior dia       :",
    pior_dia[0],
    f"({pior_dia[1]} un)"
)