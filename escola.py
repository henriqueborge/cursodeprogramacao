def cadastrar_aluno(alunos, nome, pnota, snota, tnota, qnota, media):
    aluno={
        'Nome':nome,
        'Pnota':pnota,
        'Snota':snota,
        'Tnota':tnota,
        'Qnota':qnota,
        'media':media
    }
    alunos.append(aluno)
    print("aluno cadastrado com sucesso")
def imprimir_alunos(alunos):
    for indice, aluno in enumerate (alunos):
        print(f"Alunos {indice +1}")
        print(f"Nome {aluno['Nome']}")
        print(f"Pnota {aluno['Pnota']}")
        print(f"Snota {aluno['Snota']}")
        print(f"Tnota {aluno['Tnota']}")
        print(f"Qnota {aluno['Qnota']}")
def atualizar_notas(alunos, indice, pnota, snota, tnota, qnota, media):
    if indice >= 0 and indice < len(alunos):
        alunos[indice]['Pnota']=pnota
        alunos[indice]['Snota']=snota
        alunos[indice]['Tnota']=tnota
        alunos[indice]['Qnota']=qnota
        alunos[indice]['media']=media
        print("dados do aluno atualizados com sucesso!")
    else:
        print("indice do aluno é invalido!")
def deletar_cadastro(alunos, indice):
    if indice >= 0 and indice < len(alunos):
        del alunos[indice]
        print("cadastro deletado com sucesso!")
    else:
        print("indice do aluno é invalida")
def calcular_media(alunos):
    for indice, aluno in enumerate (alunos):
        print(f"Alunos {indice +1}")
        print(f"Nome: {aluno['Nome']}")
        print(f"media: {aluno['media']}")
def alunos_aprovados(alunos):
    for indice, aluno in enumerate (alunos):
        if aluno['media'] >= 7:
            print("aluno aprovado:")
            print(f"Nome: {aluno['Nome']}")
            print(f"Media: {aluno['media']}")
def alunos_reprovados(alunos):
    for indice, aluno in enumerate (alunos):
        if aluno['media'] < 7:
            print("aluno reprovado:")
            print(f"Nome: {aluno['Nome']}")
            print(f"Media: {aluno['media']}")
        
alunos=[]

while True:
    print(" Menu\n")
    print("1. cadastrar aluno")
    print("2. imprimir alunos")
    print("3. atualizar dados")
    print("4. deletar cadastro")
    print("5. calcular media dos alunos")
    print("6. mostrar alunos aprovados")
    print("7. mostrar alunos reprovados")
    print("8. encerrar cadastro")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        nome = str(input("digite nome do aluno: "))
        pnota = float(input("digite primeira nota do aluno: "))
        snota = float(input("digite segunda nota do aluno: "))
        tnota = float(input("digite terceira nota do aluno: "))
        qnota = float(input("digite quarta nota do aluno: "))
        media=(pnota+snota+tnota+qnota)
        media = float(media/4)
        cadastrar_aluno(alunos, nome, pnota, snota, tnota, qnota, media)
    elif opcao == 2:
        imprimir_alunos(alunos)
    elif opcao == 3:
        indice = int(input("digite indice do aluno: "))
        pnota = float(input("atualize primeira nota do aluno: "))
        snota = float(input("atualize segunda nota do aluno: "))
        tnota = float(input("atualize terceira nota do aluno: "))
        qnota = float(input("atualize quarta nota do aluno: "))
        media=(pnota+snota+tnota+qnota)
        media = float(media/4)
        atualizar_notas(alunos, indice, pnota, snota, tnota, qnota, media)
    elif opcao == 4:
        indice= int(input("digite o indice do aluno: "))
        deletar_cadastro(alunos, indice)
    elif opcao == 5:
        calcular_media(alunos)
    elif opcao == 6:
        alunos_aprovados(alunos)
    elif opcao == 7:
        alunos_reprovados(alunos)
    elif opcao == 8:
        print("encerrando cadastro.")
        break
    else:
        print("opção invalida.")