salario = float(input("Digite o salário: "))
aumento = float(input("Digite o percentual de aumento: "))

novo_salario = salario + (salario * aumento / 100)

print("Novo salário:", novo_salario)