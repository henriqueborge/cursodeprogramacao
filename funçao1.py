#função para cadastro do cliente
def cadastrar_cliente(clientes, nome, email, telefone):
    cliente ={
        'Nome': nome,
        'Email': email,
        'Telefone': telefone
    }
    clientes.append(cliente)
    print("cliente cadastrado com sucesso.")
    print("************************************")
#função para imprimir dados do cliente
def imprimir_clientes(clientes):
    for indice, cliente in enumerate(clientes):
        print(f"Cliente {indice +1}")
        print(f"Nome: {cliente ['Nome']}")
        print(f"Email: {cliente ['Email']}")
        print(f"Telefone: {cliente ['Telefone']}")
        print("************************************")
def atualizar_clientes(clientes, indice, nome, email, telefone):
    if indice >= 0 and indice < len(clientes):
        clientes[indice]['Nome']= nome
        clientes[indice]['Email']= email
        clientes[indice]['Telefone']= telefone
        print("Dados atualizados com sucesso")
    else:
        print("indice do cliente invalido")
clientes = []

#Menu da função
while True:
    print("MENU\n")
    print("1. Cadastrar cliente")
    print("2. Imprimir cliente")
    print("3. atualizar cliente")
    print("4. Sair")
    
    opcao = int(input("Escolha uma opção:"))
    print("************************************")
    
    if opcao == 1:
        nome = input("digite seu nome: ")
        email = input("digite seu email: ")
        telefone = input("digite seu telefone: ")
        cadastrar_cliente(clientes, nome, email, telefone)
    elif opcao == 2:
        imprimir_clientes(clientes)
    elif opcao == 3:
        indice= int(input("digite indice do cliente: "))
        nome= input("digite novo nome: ")
        email= input("digite novo email: ")
        telefone= input("digite novo telefone: ")
        atualizar_clientes(clientes, indice, nome, email, telefone)
    elif opcao == 4:
        print("saindo.")
        break
    else:
        print("opção invalida")