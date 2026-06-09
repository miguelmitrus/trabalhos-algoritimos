lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

valor = int(input("Qual valor deseja procurar? "))

contador = 0

for numero in lista:
    if numero == valor:
        contador += 1

print("O valor aparece", contador, "vez(es).")