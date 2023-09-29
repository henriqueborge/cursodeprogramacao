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

clientes = []

#Menu da função
while True:
    print("MENU\n")
    print("1. Cadastrar cliente")
    print("2. Imprimir cliente")
    print("3. Sair")
    
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
        print("saindo.")
        break
    else:
        print("opção invalida")