lista1 = []
lista2 = []
comum = []

quantidade = int(input("Quantidade de elementos: "))

print("Primeira lista")

for i in range(quantidade):
    lista1.append(int(input("Digite um número: ")))

print("Segunda lista")

for i in range(quantidade):
    lista2.append(int(input("Digite um número: ")))

for numero in lista1:

    if numero in lista2 and numero not in comum:
        comum.append(numero)

print("Elementos em comum:", comum)