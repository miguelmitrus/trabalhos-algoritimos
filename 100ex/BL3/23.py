valor1 = bool(int(input("Digite o primeiro valor (0 ou 1): ")))
valor2 = bool(int(input("Digite o segundo valor (0 ou 1): ")))

print("AND:", valor1 and valor2)
print("OR:", valor1 or valor2)
print("NOT do primeiro:", not valor1)
print("NOT do segundo:", not valor2)