lista = []

quantidade = int(input("Quantos números terá a lista? "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

valor = int(input("Digite o valor que deseja procurar: "))

posicao = -1

for i in range(len(lista)):
    if lista[i] == valor:
        posicao = i
        break

print("Posição:", posicao)