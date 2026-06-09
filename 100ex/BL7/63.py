lista = []

for i in range(8):
    numero = int(input("Digite um número: "))
    lista.append(numero)

maior = lista[0]
posicao = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posicao = i

print("Maior valor:", maior)
print("Posição:", posicao)