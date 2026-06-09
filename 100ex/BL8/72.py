lista = []

quantidade = int(input("Quantos números terá a lista? "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

ordenada = True

for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False

if ordenada:
    print("A lista está em ordem crescente.")
else:
    print("A lista não está em ordem crescente.")