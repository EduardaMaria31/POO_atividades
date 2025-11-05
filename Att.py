#Atividade: Criar um programa que receba dados do usuários como nome e idade, deverá usar o bloco
#try...except para tratar o erro caso o usuário digite letra quando informar idade.
#E tratar nome quando o usuário digitar número ou vazio quando informar o nome.


def mostrar_nome():
        while True:
            nome = input("Digite seu nome:")
            if not nome.strip():
                print("Seu campo nome não pode estar vazio.")
            elif nome.isnumeric():
                print("O nome não pode conter números.")
            else:
                return nome

def mostar_idade():
        while True:
            try:
                idade = int(input("Digite sua idade:"))
                return idade
            except ValueError:
                print("Idade inválida! Apenas números será aceito.")


nome = mostrar_nome()
idade = mostar_idade()

print(f"Nome = {nome}")
print(f"Idade: {idade}")



