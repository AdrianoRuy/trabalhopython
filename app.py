import os

# Função para exibir o menu
def exibir_menu():
    print("\n--- Lista de Supermercado ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Salvar lista")
    print("5. Carregar lista")
    print("6. Sair")

# Função para adicionar item
def adicionar_item(lista):
    item = input("Digite o nome do item a ser adicionado: ")
    lista.append(item)
    print(f"Item '{item}' adicionado com sucesso!")

# Função para remover item
def remover_item(lista):
    item = input("Digite o nome do item a ser removido: ")
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' removido com sucesso!")
    else:
        print(f"Item '{item}' não encontrado na lista.")

# Função para exibir a lista de itens
def exibir_lista(lista):
    if lista:
        print("\nSua lista de supermercado:")
        for idx, item in enumerate(lista, 1):
            print(f"{idx}. {item}")
    else:
        print("A lista está vazia.")

# Função para salvar a lista em um arquivo
def salvar_lista(lista, arquivo="lista_supermercado.txt"):
    with open(arquivo, "w") as f:
        for item in lista:
            f.write(item + "\n")
    print(f"Lista salva com sucesso em '{arquivo}'.")

# Função para carregar a lista de um arquivo
def carregar_lista(arquivo="lista_supermercado.txt"):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            lista = [linha.strip() for linha in f.readlines()]
        print(f"Lista carregada com sucesso de '{arquivo}'.")
        return lista
    else:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
        return []

# Função principal
def main():
    lista = []
    carregar = input("Você deseja carregar a lista salva anteriormente? (s/n): ").strip().lower()
    if carregar == 's':
        lista = carregar_lista()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            remover_item(lista)
        elif opcao == "3":
            exibir_lista(lista)
        elif opcao == "4":
            salvar_lista(lista)
        elif opcao == "5":
            lista = carregar_lista()
        elif opcao == "6":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()

