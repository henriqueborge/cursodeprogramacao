import openpyxl

def cadastrar_xlsx(nome_arquivo):
    try:
        # Carrega o arquivo XLSX
        workbook = openpyxl.load_workbook(nome_arquivo)
        
        # Selecione a planilha que deseja ler (por nome ou índice)
        planilha = workbook.active  # A planilha ativa (normalmente a primeira) por padrão

        # Crie uma lista para armazenar os dados
        dados = []

        # Itera pelas linhas da planilha
        for linha in planilha.iter_rows(values_only=True):
            dados.append(linha)

        return dados
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo XLSX: {str(e)}")
        return None

# Exemplo de uso da função:
nome_arquivo = "excel.xlsx"
dados = cadastrar_xlsx(nome_arquivo)

if dados is not None:
    # Agora você pode usar a lista 'dados' para trabalhar com os dados da planilha
    for linha in dados:
        print(linha)
