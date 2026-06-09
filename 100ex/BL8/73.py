lista = []

quantidade = int(input("Quantos números terá a lista? "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

maior = max(lista)

segundo = None

for numero in lista:
    if numero != maior:
        if segundo is None or numero > segundo:
            segundo = numero

print("Segundo maior valor:", segundo)