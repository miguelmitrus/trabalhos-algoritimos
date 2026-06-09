lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

nova_lista = []

for numero in lista:
    if numero not in nova_lista:
        nova_lista.append(numero)

print("Lista sem repetição:", nova_lista)