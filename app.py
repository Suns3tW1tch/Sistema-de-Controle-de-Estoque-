def mostrar_menu():
    print("\n=== SISTEMA DE CONTROLE DE ESTOQUE ===")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("0 - Sair")

def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("Nome do produto não pode ser vazio.")
        return

    if nome in estoque:
        print("Produto já existe no estoque.")
        return

    try:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade em estoque: "))

        if preco <= 0 or quantidade < 0:
            print("Preço e quantidade devem ser valores positivos.")
            return

    except ValueError:
        print("Preço ou quantidade inválidos.")
        return

    estoque[nome] = {
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"Produto '{nome}' adicionado com sucesso!")

def atualizar_produto(estoque):
    nome = input("Nome do produto a atualizar: ").strip()

    if nome == "":
        print("Nome do produto não pode ser vazio.")
        return

    if nome not in estoque:
        print("Produto não encontrado no estoque.")
        return

    try:
        preco = float(input("Novo preço do produto: "))
        quantidade = int(input("Nova quantidade em estoque: "))

        if preco <= 0 or quantidade < 0:
            print("Preço e quantidade devem ser valores válidos.")
            return

    except ValueError:
        print("Preço ou quantidade inválidos.")
        return

    estoque[nome]["preco"] = preco
    estoque[nome]["quantidade"] = quantidade

    print(f"Produto '{nome}' atualizado com sucesso!")

def excluir_produto(estoque):
    nome = input("Nome do produto a excluir: ").strip()

    if nome == "":
        print("Nome do produto não pode ser vazio.")
        return

    if nome not in estoque:
        print("Produto não encontrado no estoque.")
        return

    del estoque[nome]
    print(f"Produto '{nome}' excluído com sucesso!")

def visualizar_estoque(estoque):
    if not estoque:
        print("\nEstoque vazio.")
        return

    print("\n=== ESTOQUE ATUAL ===")
    for nome, dados in estoque.items():
        print(f"Produto: {nome}")
        print(f"Preço: R$ {dados['preco']:.2f}")
        print(f"Quantidade: {dados['quantidade']}")
        print("-" * 30)

def main():
    estoque = {
        "Notebook": {"preco": 3500.00, "quantidade": 10},
        "Mouse": {"preco": 120.00, "quantidade": 25}
    }
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            atualizar_produto(estoque)
        elif opcao == "3":
            excluir_produto(estoque)
        elif opcao == "4":
            visualizar_estoque(estoque)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

main()
