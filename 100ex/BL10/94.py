def mostrar_lista(lista):

    for i in range(len(lista)):
        print("Índice:", i, "- Valor:", lista[i])


numeros = []

for i in range(5):
    numeros.append(int(input("Digite um número: ")))

mostrar_lista(numeros)