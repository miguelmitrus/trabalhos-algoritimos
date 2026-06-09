def eh_par(numero):

    if numero % 2 == 0:
        return True
    else:
        return False


valor = int(input("Digite um número: "))

print(eh_par(valor))