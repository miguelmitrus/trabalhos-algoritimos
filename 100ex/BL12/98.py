class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)


nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

pessoa = Pessoa(nome, idade)

pessoa.exibir_dados()