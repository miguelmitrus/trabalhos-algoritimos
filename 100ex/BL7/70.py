notas = []

quantidade = int(input("Quantas notas serão digitadas? "))

for i in range(quantidade):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

contador = 0

for nota in notas:
    if nota > media:
        contador += 1

print("Média da turma:", media)
print("Quantidade de alunos acima da média:", contador)