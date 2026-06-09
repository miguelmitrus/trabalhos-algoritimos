def media(lista):

    soma = 0

    for numero in lista:
        soma += numero

    return soma / len(lista)


numeros = []

for i in range(5):
    numeros.append(float(input("Digite um número: ")))

print("Média:", media(numeros))