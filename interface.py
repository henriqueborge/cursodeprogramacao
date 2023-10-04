import csv
def cadastrar_cliente(clientes, nome, email, telefone):
    cliente = {
        'nome':nome,
        'email':email,
        'telefone':telefone
    }
    clientes.append(cliente)
    print("cliente cadastrado com sucesso")
def ler_dados_csv():
    with open('arquivo.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            print(f"Nome: {linha['nome']}, Email: {linha['email']}, Telefone: {linha['telefone']}")
        

clientes = []

while True:
    print(" Menu\n")
    print("1. cadastrar cliente")
    print("2. ler dados do cliente")
    print("3. sair")
    
    opcao = int(input("escolha uma opção: "))
    
    if opcao == 1:
        nome=input("digite nome: ")
        email=input("digite email: ")
        telefone=input("digite telefone: ")
        cadastrar_cliente(clientes, nome, email, telefone)
        with open('arquivo.csv', mode="w", newline="") as arquivo_csv:
    
            writer = csv.writer(arquivo_csv)
    
            writer.writerow(["nome", "email", "telefone",])
    
            for cliente in clientes:
                writer.writerow([cliente["nome"], cliente["email"], cliente["telefone"]])
    elif opcao == 2:
        ler_dados_csv()
    elif opcao == 3:
        print("saindo")
        break
    else:
        print("opção invalida")
