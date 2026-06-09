lista = []
quadrados = []

for i in range(7):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for numero in lista:
    quadrados.append(numero ** 2)

print("Lista original:", lista)
print("Quadrados:", quadrados)