lista = []

quantidade = int(input("Quantos números serão digitados? "))

for i in range(quantidade):
    lista.append(int(input("Digite um número: ")))

verificados = []

for numero in lista:

    if numero not in verificados:

        contador = 0

        for elemento in lista:
            if elemento == numero:
                contador += 1

        print(numero, "aparece", contador, "vez(es).")

        verificados.append(numero)