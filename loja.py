produto=[]
valor=[]
qtd=[]
imp1=[]
imp2=[]
ipm3=[]
frete=[]
lucro=[]
while True:
    menu = int(input(
        "escolha uma opção do menu\n"
        "1 - inserir\n"
        "2 - imprimir\n"
        "3 - atualizar\n"
        "4 - deletar\n"
        "5 - calcular"
        "6 - sair\n"
    ))

    if menu == 1:
        produto = input("digite o nome do produto: ")
        valor = input("digite valor do produto: ")
        qtd = input("digite a quantidade do produto: ")
        imp1 = input("digte valor do primeiro imposto: ")
        imp2 = input("digte valor do segundo imposto: ")
        imp3 = input("digte valor do terceiro imposto: ")
        frete = input("digite valor do frete: ")
        lucro = input("digite o seu lucro: ")
        produto.__add__(produto)
        valor.__add__(valor)
        qtd.__add__(qtd)
        imp1.__add__(imp1)
        imp2.__add__(imp2)
        imp3.__add__(imp3)
        frete.__add__(frete)
        lucro.__add__(lucro)
        print("item listado com sucesso")
    elif menu == 2:
        print("lista de produtos")
        for a in range (len(produto)):
            print(f"{produto[a]}  {qtd[a]} {imp1[a]} {imp2[a]} {imp3[a]} {frete[a]} {lucro[a]}")
    elif menu == 3:
        produto_para_atualizar = input("digite nome do produto: ")
        if produto_para_atualizar in produto:
            indice = produto.index(produto_para_atualizar)
            novo_valor = input("digite novo valor: ")
            valor[indice]= novo_valor
            print("valor atualizado com sucesso.")
        else:
            print("nome do produto não encontrado")
    elif menu == 4:
        produto_para_deletar = input("digite nome do produto: ")
        if produto_para_deletar in produto:
            indice = produto.index(produto_para_deletar)
            del produto[indice]
            del valor[indice]
            del qtd[indice]
            del imp1[indice]
            del imp2[indice]
            del imp3[indice]
            del frete[indice]
            del lucro[indice]
            print("produto deletado com sucesso.")
        else:
            print("produto não encontrado.")
    elif menu == 5:
        produto_para_calcular= input("digite o nome do produto: ")
        if produto_para_calcular in produto:
            indice= produto.index(produto_para_calcular)
            valorfrete=frete/qtd[indice]
            impa=valor*imp1[indice]
            impb=valor*imp2[indice]
            impc=valor*imp3[indice]
            pc=valor+impa+impb+impc+valorfrete[indice]
            pv=pc*lucro
            print("produto: {produto} valor {valor} preço custo {pc} preço de venda {pv}")
        else:
            print("este item não existe na lista")
    elif menu == 6:
        print("saindo do programa.")
        break
    else:
        print("opção invalida, tente outra opção.")