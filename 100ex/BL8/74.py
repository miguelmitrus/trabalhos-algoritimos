lista = []
positivos = []
negativos = []

quantidade = int(input("Quantos números serão digitados? "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

for numero in lista:

    if numero >= 0:
        positivos.append(numero)

    else:
        negativos.append(numero)

print("Positivos:", positivos)
print("Negativos:", negativos)