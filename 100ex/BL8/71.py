lista = []

quantidade = int(input("Quantos números terá a lista? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    lista.append(numero)

ultimo = lista[-1]

for i in range(len(lista) - 1, 0, -1):
    lista[i] = lista[i - 1]

lista[0] = ultimo

print(lista)