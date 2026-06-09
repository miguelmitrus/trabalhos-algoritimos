def calcular_total(valores):
    return sum(valores)


def calcular_media(valores):
    return sum(valores) / len(valores)


def encontrar_maior(valores, nomes):

    maior = valores[0]
    indice = 0

    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
            indice = i

    return nomes[indice], maior


def encontrar_menor(valores, nomes):

    menor = valores[0]
    indice = 0

    for i in range(len(valores)):
        if valores[i] < menor:
            menor = valores[i]
            indice = i

    return nomes[indice], menor


def calcular_percentual(valor, total):

    if total == 0:
        return 0

    return round((valor / total) * 100, 1)


def formatar_linha(nome, total, media, percentual=None):

    if percentual is None:
        return f"{nome:<12} | Total: {total:>3} un | Média: {media:.1f}"

    return f"{nome:<12} | Total: {total:>3} un | Média: {media:.1f} | {percentual:.1f}%"