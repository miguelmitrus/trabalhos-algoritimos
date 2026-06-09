lista1 = []
lista2 = []
lista3 = []

print("Primeira lista")

for i in range(5):
    lista1.append(int(input("Digite um número: ")))

print("Segunda lista")

for i in range(5):
    lista2.append(int(input("Digite um número: ")))

for i in range(5):
    lista3.append(lista1[i] + lista2[i])

print("Terceira lista:", lista3)