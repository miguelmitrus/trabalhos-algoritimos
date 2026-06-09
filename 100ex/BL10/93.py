def contar_vogais(texto):

    contador = 0

    for letra in texto.lower():

        if letra in "aeiou":
            contador += 1

    return contador


frase = input("Digite uma palavra ou frase: ")

print("Quantidade de vogais:", contar_vogais(frase))