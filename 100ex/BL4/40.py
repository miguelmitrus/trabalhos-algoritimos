nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência (%): "))

media = (nota1 + nota2) / 2

if media >= 7 and frequencia >= 75:
    print("Aluno aprovado.")

elif media < 7 and frequencia >= 75:
    print("Reprovado por nota.")

elif media >= 7 and frequencia < 75:
    print("Reprovado por frequência.")

else:
    print("Reprovado por nota e frequência.")