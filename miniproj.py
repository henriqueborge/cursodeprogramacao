#criação do objeto
cliente = {
    "nome": str,
    "cpf": str,
    "idade": int
}
#função para registro de cliente
def registrar_dados(nome,cpf,idade):
    nome=input("digite seu nome")
    cpf=input("digite seu cpf")
    idade=input("digite sua idade")
    if cpf == cpf:
        print("cliente ja registrado.")
    else:
        print("cliente registrado com sucesso.")
#função para impressão de dados do cliente
def imprimir_dados_do_cliente(nome,cpf,idade):
    if cpf == cpf:
        print("seus dados:\n")
        print(nome)
        print(cpf)
        print(idade)
    else:
        print("cliente não registrado.")
#função para atualizar dados do cliente
def atualizar_dados_do_cliente(nome,cpf,idade):
    if cpf == cpf:
        print("atualize seus dados:")
        nome=input("digite nome")
        cpf=input("digite cpf")
        idade=input("digite idade")
    else:
        print("cliente não existe.")
#função para deletar usuario
def deletar_dados_do_cliente(nome,cpf,idade):
    if cpf == cpf:
        print("dados serão deletados.")
        del nome
        del cpf
        del idade
    else:
        print("cliente não existe.")