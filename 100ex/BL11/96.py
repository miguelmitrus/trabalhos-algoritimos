def soma_naturais(n):

    if n == 0:
        return 0

    return n + soma_naturais(n - 1)


numero = int(input("Digite um número: "))

print("Soma:", soma_naturais(numero))