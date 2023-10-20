# Funções:
def mostrar_menu_principal():
    """
    Apresenta as opções do menu na tela.
    :return: Opção do menu escolhida pelo usuário.
    """
    print("----MENU PRINCIPAL!----")
    print("1 - Disciplinas")
    print("2 - Estudantes")
    print("3 - Matriculas")
    print("4 - Professores")
    print("5 - Turmas")
    print("0 - Sair")

    return input("Digite o número da opção desejada (0 para finalizar): ")


def mostrar_submenu():
    """
    Mostra na tela as opções do menu de operações (submenu)
    :return: Operação escolida pelo usuário.
    """
    print("1 - Cadastrar")
    print("2 - Editar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Voltar ao menu anterior")

    return input("Digite o número da opção desejada: ")


def cadastrar_aluno(estudantes):
    """
    Adiciona um aluno a lista estudantes
    :param estudantes: Lista já criada
    :return:
    """
    codigo = int(input("Digite o codigo do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite cpf do estudante: ")
    dicionario_estudantes = {}
    dicionario_estudantes["codigo aluno"] = codigo
    dicionario_estudantes["nome aluno"] = nome
    dicionario_estudantes["cpf aluno"] = cpf
    estudantes.append(dicionario_estudantes)
    print("Novo estudante cadastrado com sucesso! Voltando a pagina anterior.")


def editar_aluno(estudantes):
    """
    Edita um aluno existente na lista estudantes ou avisa caso não exista um aluno com o código inserido
    :param estudantes: Lista já criada
    """
    estudante_para_editar = None
    codigo_de_edicao = int(input("Qual é o código do aluno que deseja editar? "))
    for dicionario_estudantes in estudantes:
        if dicionario_estudantes["codigo aluno"] == codigo_de_edicao:
            estudante_para_editar = dicionario_estudantes
            break
    if estudante_para_editar is None:
        print("Não foi possivel localizar um aluno com esse código")
    else:
        novo_codigo = int(input("Digite um código para o estudante: "))
        novo_nome = input("Digite um nome para o estudante: ")
        novo_cpf = input("Digite cpf do estudante: ")
        estudante_para_editar["codigo aluno"] = novo_codigo
        estudante_para_editar["nome aluno"] = novo_nome
        estudante_para_editar["cpf aluno"] = novo_cpf
        print("Estudante editado com sucesso! Voltando a pagina anterior.")


def excluir_aluno(estudantes):
    """
        Exclui um aluno existente na lista estudantes ou avisa caso não exista um aluno com o código inserido
        :param estudantes: Lista já criada
        """
    estudante_para_remover = None
    codigo_de_exclusao = int(input("Qual é o código do aluno que deseja excluir? "))
    for dicionario_estudantes in estudantes:
        if dicionario_estudantes["codigo aluno"] == codigo_de_exclusao:
            estudante_para_remover = dicionario_estudantes
            break
    if estudante_para_remover is None:
        print("Não foi possivel localizar um aluno com esse código")
    else:
        estudantes.remove(estudante_para_remover)
        print("Registro excluido com sucesso")


def listar_alunos(estudantes):
    """
        Mostra os dados da lista estudantes ou avisa se a lista estiver vazia
        :param estudantes: Lista já criada
        """
    if not estudantes:
        print("Ainda não existe estudantes cadastrados!")
    for elemento in estudantes:
        print(elemento)


# Listas:
estudantes = [
    {"codigo aluno": 1, "nome aluno": "Lucas", "cpf aluno": "999"},
    {"codigo aluno": 2, "nome aluno": "Pedro", "cpf aluno": "555"}
]

# Funcionamento do programa:
while True:
    # Menu
    opcao_principal = mostrar_menu_principal()
    print(f"Você escolheu a opção {opcao_principal}")
    # Opções em desenvolvimento
    if opcao_principal == "1" or opcao_principal == "3" or opcao_principal == "4" or opcao_principal == "5":
        print("!EM DESENVOLVIMENTO!")
    # Submenu estudantes
    elif opcao_principal == "2":
        print(f"---Menu de Estudantes---")
        while True:
            # Submenu
            operacao = mostrar_submenu()
            print(f"Você escolheu a opção {operacao}")
            if operacao == "1":
                cadastrar_aluno(estudantes)
            elif operacao == "2":
                editar_aluno(estudantes)
            elif operacao == "3":
                excluir_aluno(estudantes)
            elif operacao == "4":
                listar_alunos(estudantes)
            elif operacao == "5":
                break
            else:
                print(f"Opção {operacao} invalida!")
    # Menu principal = 0 sair
    elif opcao_principal == "0":
        break
    # Mensagem opção invalida do menu principal
    else:
        print(f"Opção {opcao_principal} invalida!")
