#função para cadastro do produto
def cadastrar_produto(produtos, nome, valor, quantidade, imp1, imp2, imp3, frete, custo, lucro, venda ):
    produto = {
        'Nome':nome,
        'Valor':valor,
        'Quantidade':quantidade,
        'imposto1': imp1,
        'imposto2': imp2,
        'imposto3': imp3,
        'Frete': frete,
        'Custo': custo,
        'lucro': lucro,
        'venda': venda
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
        print(f"imposto1: {produto ['imposto1']}")
        print(f"imposto2: {produto ['imposto2']}")
        print(f"imposto3: {produto ['imposto3']}")
        print(f"Frete: {produto ['Frete']}")
        print(f"Custo: {produto ['Custo']}")
        print(f"venda: {produto ['venda']}")
        print(f"lucro: {produto ['lucro']}")
def atualizar_produto(produtos, indice, nome, valor, quantidade, imp1, imp2, imp3, frete, custo, lucro, venda):
    if indice >= 0 and indice < len(produtos):
        produtos[indice]['Nome']=nome
        produtos[indice]['Valor']=valor
        produtos[indice]['Quantidade']=quantidade
        produtos[indice]['imposto1']=imp1
        produtos[indice]['imposto2']=imp2
        produtos[indice]['imposto3']=imp3
        produtos[indice]['Frete']=frete
        produtos[indice]['Custo']=custo
        produtos[indice]['lucro']=lucro
        produtos[indice]['venda']=venda
        print("dados do produto atualizado com sucesso")
    else:
        print("indice do produto invalido")
def deletar_produto(produtos, indice,):
    if indice >= 0 and indice < len(produtos):
        del produtos[indice]
        print("produto deletado com sucesso")
    else:
        print("indice do produto não existe")
produtos = []

#Menu da função
while True:
    print("MENU\n")
    print("1. cadastrar produto")
    print("2. imprimir produto")
    print("3. atualizar produto")
    print("4. deletar produto")
    print("5. sair")
    
    opcao = int(input("Escolha uma opção"))
    
    print("************************************")
    
    if opcao == 1:
        nome = input("digite o nome do produto: ")
        valor = float(input("digite valor do produto: "))
        quantidade = int(input("digite a quantidade: "))
        imp1 = float(input("digite o primeiro imposto: "))
        imp2 = float(input("digite o segundo imposto: "))
        imp3 = float(input("digite o terceiro imposto: "))
        frete = int(input("digite valor do frete: "))
        lucro = float(input("digite quanto deseja de lucro: "))
        imp1=((valor*imp1)/100)
        imp2=((valor*imp2)/100)
        imp3=((valor*imp3)/100)
        valorfrete=frete/quantidade
        custo = (valor+imp1+imp2+imp3+valorfrete)
        lucro = ((custo*lucro)/100)
        venda = custo+lucro
        cadastrar_produto(produtos, nome, valor, quantidade, imp1, imp2, imp3, frete,custo,lucro,venda)
    elif opcao == 2:
        imprimir_produtos(produtos)
    elif opcao == 3:
        indice= int(input("digite indice do produto"))
        nome= input("digite novo nome do produto")
        valor = float(input("digite novo valor do produto: "))
        quantidade = int(input("digite a nova quantidade: "))
        imp1 = float(input("digite o primeiro imposto: "))
        imp2 = float(input("digite o segundo imposto: "))
        imp3 = float(input("digite o terceiro imposto: "))
        frete = int(input("digite valor do frete: "))
        lucro = float(input("digite quanto deseja de lucro: "))
        imp1=((valor*imp1)/100)
        imp2=((valor*imp2)/100)
        imp3=((valor*imp3)/100)
        valorfrete=frete/quantidade
        custo = (valor+imp1+imp2+imp3+valorfrete)
        lucro = ((custo*lucro)/100)
        venda = custo+lucro
        atualizar_produto(produtos, indice, nome, valor, quantidade, imp1, imp2, imp3, frete, custo, lucro, venda)
    elif opcao == 4:
        indice= int(input("digite indice do produto"))
        deletar_produto(produtos, indice)
    elif opcao == 5:
        print("saindo.")
        break
    else:
        print("opção invalida")