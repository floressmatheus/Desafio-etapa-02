# Primeiramente deve criar um banco de dados listando os personagens criados
personagens = {}

# Função para adicionar novo personagem a lista
def adicionar_personagens():
    nome = input("Crie um nome para o seu personagem: ")
    descricao = input("Descreva um pouco sobre o seu personagem: ")
    imagem = input("Digite um link de uma imagem para representar seu personagem: ")
    programa = input("Digite o programa do seu personagem: ")
    animador = input("Digite o animador do seu personagem: ")
    personagens[nome] = {"descrição": descricao, "imagem": imagem, "programa": programa, "animador": animador}

# Função para visualizar personagens da lista
def visualizar_personagens():
    for nome, info in personagens.items():
        print(f"{nome}: {info['descrição']} ({info['programa']}, animado por {info['animador']})\n{info['imagem']}\n")

# Executar o progreama principal, um looping que permite o usuário a criar e visualisar personagens
while True:
    acao = input("Para criar novo personagem digite 'N' e para visualisar personagem digite 'V': ")
    if acao == "N":
        adicionar_personagens()
    elif acao == "V":
        visualizar_personagens()
    else:
        break    
     
