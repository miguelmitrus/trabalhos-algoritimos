primeiro = int(input("Digite um número: "))
maior = primeiro
menor = primeiro

for i in range(9):
    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Maior valor:", maior)
print("Menor valor:", menor)