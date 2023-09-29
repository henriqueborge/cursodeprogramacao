#função para cadastro do produto
def cadastrar_produto(produtos, nome, valor, quantidade,):
    produto = {
        'Nome':nome,
        'Valor':valor,
        'Quantidade':quantidade
    }
    produtos.append(produto)
    print("produto cadastrado com sucesso.")
    print("************************************")
#função para imprimir produto
def imprimir_produtos(produtos):
    for indice, produto in enumerate(produtos):
        print(f"Produtos {indice +1}")
        print(f"Nome: {produto ['Nome']}")
        print(f"Valor: {produto ['Valor']}")
        print(f"Quantidade: {produto ['Quantidade']}")
def valor_total(produtos):
    for indice in enumerate(produtos):
        print(valor * quantidade)
        print("****************************")
        
produtos = []

#Menu da função
while True:
    print("MENU\n")
    print("1. cadastrar produto")
    print("2. imprimir produto")
    print("3. sair")
    
    opcao = int(input("Escolha uma opção"))
    
    print("************************************")
    
    if opcao == 1:
        nome = input("digite o nome do produto")
        valor = float(input("digite valor do produto"))
        quantidade = int(input("digite a quantidade"))
        cadastrar_produto(produtos, nome, valor, quantidade)
    elif opcao == 2:
        imprimir_produtos(produtos)
        valor_total(produtos)
    elif opcao == 3:
        print("saindo.")
        break
    else:
        print("opção invalida")