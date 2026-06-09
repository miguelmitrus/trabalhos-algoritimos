lista = []
pares = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print("Lista original:", lista)
print("Lista de pares:", pares)