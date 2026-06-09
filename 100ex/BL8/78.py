lista = []
acumulada = []

quantidade = int(input("Quantos números terá a lista? "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

soma = 0

for numero in lista:
    soma += numero
    acumulada.append(soma)

print("Lista original:", lista)
print("Soma acumulada:", acumulada)