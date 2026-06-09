def imprimir_arvore(no, nivel=0):
    print("  " * nivel + f"{no['nome']} ({no['idade']} anos)")

    for filho in no["filhos"]:
        imprimir_arvore(filho, nivel + 1)


def contar_descendentes(no):
    if len(no["filhos"]) == 0:
        return 0

    total = 0

    for filho in no["filhos"]:
        total += 1 + contar_descendentes(filho)

    return total


def buscar_personagem(no, nome):
    if no["nome"] == nome:
        return no

    for filho in no["filhos"]:
        resultado = buscar_personagem(filho, nome)

        if resultado is not None:
            return resultado

    return None


def calcular_geracao(no, nome, geracao=0):
    if no["nome"] == nome:
        return geracao

    for filho in no["filhos"]:
        resultado = calcular_geracao(filho, nome, geracao + 1)

        if resultado != -1:
            return resultado

    return -1


def listar_nomes(no):
    nomes = [no["nome"]]

    for filho in no["filhos"]:
        nomes += listar_nomes(filho)

    return nomes


def maior_idade(no):
    mais_velho = no

    for filho in no["filhos"]:
        candidato = maior_idade(filho)

        if candidato["idade"] > mais_velho["idade"]:
            mais_velho = candidato

    return mais_velho