from utils import *

familia = {
    "nome": "Aldo",
    "idade": 80,
    "filhos": [

        {
            "nome": "Beatriz",
            "idade": 55,
            "filhos": [

                {
                    "nome": "Daniel",
                    "idade": 30,
                    "filhos": []
                },

                {
                    "nome": "Elisa",
                    "idade": 27,
                    "filhos": [

                        {
                            "nome": "Hugo",
                            "idade": 5,
                            "filhos": []
                        }

                    ]
                }

            ]
        },

        {
            "nome": "Carlos",
            "idade": 52,
            "filhos": [

                {
                    "nome": "Fernanda",
                    "idade": 25,
                    "filhos": []
                },

                {
                    "nome": "Gabriel",
                    "idade": 22,
                    "filhos": []
                }

            ]
        },

        {
            "nome": "Diana",
            "idade": 48,
            "filhos": [

                {
                    "nome": "Isabela",
                    "idade": 20,
                    "filhos": []
                }

            ]
        }

    ]
}

print("===== ARVORE GENEALOGICA =====\n")

imprimir_arvore(familia)

print("\n==============================\n")

nome = input("Digite o nome do personagem: ")

personagem = buscar_personagem(familia, nome)

if personagem is not None:

    print("\nPersonagem encontrado:")
    print("Nome:", personagem["nome"])
    print("Idade:", personagem["idade"], "anos")
    print("Geração:", calcular_geracao(familia, nome))
    print("Descendentes:", contar_descendentes(personagem))

else:

    print("\nPersonagem não encontrado.")

nomes = listar_nomes(familia)

print("\nTodos os membros:")
print(", ".join(nomes))

print("\nTotal de membros:", len(nomes))

mais_velho = maior_idade(familia)

print(
    "Membro mais velho:",
    mais_velho["nome"],
    f"({mais_velho['idade']} anos)"
)

print(
    "Descendentes de Aldo:",
    contar_descendentes(familia)
)