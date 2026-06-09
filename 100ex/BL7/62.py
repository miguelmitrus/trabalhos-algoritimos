lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

soma = sum(lista)
media = soma / len(lista)

print("Soma:", soma)
print("Média:", media)