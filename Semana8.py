# Import
import json


# Funções:
def mostrar_menu_principal():
    """
    Apresenta as opções do menu na tela.
    :return: Opção do menu escolhida pelo usuário.
    """
    print("----MENU PRINCIPAL!----\n1 - Disciplinas\n2 - Estudantes\n3 - Matriculas\n4 - Professores \
    \n5 - Turmas\n0 - Sair")
    return input("Digite o número da opção desejada (0 para finalizar): ")


def mostrar_submenu():
    """
    Mostra na tela as opções do menu de operações (submenu)
    :return: Operação escolida pelo usuário.
    """
    print("1 - Cadastrar\n2 - Editar\n3 - Excluir\n4 - Listar\n5 - Voltar ao menu anterior")

    return input("Digite o número da opção desejada: ")


def cadastrar(nome_arquivo, opcao_menu_principal):
    """
    Adiciona um aluno a lista estudantes
    :param nome_arquivo: arquivo json
    :return:
    """
    if opcao_menu_principal == "1":
        codigo = int(input("Digite o código da disciplina: "))
        nome = input("Digite o nome da disciplina: ")
        dicionario_nova_disciplina = {"Código da disciplina": codigo, "Nome da disciplina": nome}
        quem_irei_cadastrar = ler_arquivo_json(nome_arquivo)
        quem_irei_cadastrar.append(dicionario_nova_disciplina)
        salvar_arquivo_json(quem_irei_cadastrar, nome_arquivo)
        print(f"Disciplina de {nome} cadastrada com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "2":
        codigo = int(input("Digite o código do estudante: "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite cpf do estudante: ")
        dicionario_novo_estudante = {"Código aluno": codigo, "Nome aluno": nome, "CPF aluno": cpf}
        quem_irei_cadastrar = ler_arquivo_json(nome_arquivo)
        quem_irei_cadastrar.append(dicionario_novo_estudante)
        salvar_arquivo_json(quem_irei_cadastrar, nome_arquivo)
        print(f"Aluno(a) {nome} cadastrado(a) com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "3":
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        dicionario_nova_matricula = {"Código turma": codigo_turma, "Código aluno": codigo_estudante}
        quem_irei_cadastrar = ler_arquivo_json(nome_arquivo)
        quem_irei_cadastrar.append(dicionario_nova_matricula)
        salvar_arquivo_json(quem_irei_cadastrar, nome_arquivo)
        print(f"Matricula do aluno(a) código {codigo_estudante} cadastrada com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "4":
        codigo = int(input("Digite o código do professor: "))
        nome = input("Digite o nome do professor: ")
        cpf = input("Digite cpf do professor: ")
        dicionario_novo_professor = {"Código do professor": codigo, "Nome do professor": nome, "CPF do professor": cpf}
        quem_irei_cadastrar = ler_arquivo_json(nome_arquivo)
        quem_irei_cadastrar.append(dicionario_novo_professor)
        salvar_arquivo_json(quem_irei_cadastrar, nome_arquivo)
        print(f"Professor(a) {nome} cadastrado(a) com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "5":
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_professor = int(input("Digite o código do professor(a): "))
        codigo_disciplina = input("Digite o código da disciplina: ")
        dicionario_novo_estudante = {"Código da turma": codigo_turma, "Código do professor": codigo_professor, "Código\
         da disciplina": codigo_disciplina}
        quem_irei_cadastrar = ler_arquivo_json(nome_arquivo)
        quem_irei_cadastrar.append(dicionario_novo_estudante)
        salvar_arquivo_json(quem_irei_cadastrar, nome_arquivo)
        print(f"Tuma número {codigo_turma} cadastrada com sucesso! Voltando a pagina anterior.")


def editar(nome_arquivo, opcao_menu_principal):
    """
    Edita um aluno existente na lista estudantes ou avisa caso não exista um aluno com o código inserido
    :param nome_arquivo: arquivo json
    """
    if opcao_menu_principal == "1":
        disciplina_para_editar = None
        codigo_de_edicao = int(input("Qual é o código da disciplina que deseja editar? "))
        oque_irei_editar = ler_arquivo_json(nome_arquivo)
        for dicionario in oque_irei_editar:
            if dicionario["Código da disciplina"] == codigo_de_edicao:
                disciplina_para_editar = dicionario
                break
        if disciplina_para_editar is None:
            print("Não foi possivel localizar uma disciplina com esse código")
        else:
            novo_nome = input("Digite o novo nome para disciplina: ")
            disciplina_para_editar["Nome da disciplina"] = novo_nome
            salvar_arquivo_json(oque_irei_editar, nome_arquivo)
            print("Disciplina editada com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "2":
        estudante_para_editar = None
        codigo_de_edicao = int(input("Qual é o código do aluno que deseja editar? "))
        quem_irei_editar = ler_arquivo_json(nome_arquivo)
        for dicionario in quem_irei_editar:
            if dicionario["Código aluno"] == codigo_de_edicao:
                estudante_para_editar = dicionario
                break
        if estudante_para_editar is None:
            print("Não foi possivel localizar um aluno com esse código")
        else:
            novo_nome = input("Digite um nome para o estudante: ")
            novo_cpf = input("Digite cpf do estudante: ")
            estudante_para_editar["Nome aluno"] = novo_nome
            estudante_para_editar["CPF aluno"] = novo_cpf
            salvar_arquivo_json(quem_irei_editar, nome_arquivo)
            print("Estudante editado com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "3":
        matricula_para_editar = None
        codigo_de_edicao = int(input("Qual é o código da turma em que deseja editar a matricula? "))
        oque_irei_editar = ler_arquivo_json(nome_arquivo)
        for dicionario in oque_irei_editar:
            if dicionario["Código turma"] == codigo_de_edicao:
                matricula_para_editar = dicionario
                break
        if matricula_para_editar is None:
            print("Não foi possivel localizar uma turma com esse código")
        else:
            novo_aluno = int(input("Digite o novo codigo do aluno referente a essa matricula: "))
            matricula_para_editar["Código aluno"] = novo_aluno
            salvar_arquivo_json(oque_irei_editar, nome_arquivo)
            print("Estudante editado com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "4":
        professor_para_editar = None
        codigo_de_edicao = int(input("Qual é o código do professor que deseja editar? "))
        quem_irei_editar = ler_arquivo_json(nome_arquivo)
        for dicionario in quem_irei_editar:
            if dicionario["Código do professor"] == codigo_de_edicao:
                professor_para_editar = dicionario
                break
        if professor_para_editar is None:
            print("Não foi possivel localizar um professor com esse código")
        else:
            novo_nome = input("Digite um nome para o professor: ")
            novo_cpf = input("Digite o cpf do professor: ")
            professor_para_editar["Nome do professor"] = novo_nome
            professor_para_editar["CPF do professor"] = novo_cpf
            salvar_arquivo_json(quem_irei_editar, nome_arquivo)
            print("Professor editado com sucesso! Voltando a pagina anterior.")
    elif opcao_menu_principal == "5":
        turma_para_editar = None
        codigo_de_edicao = int(input("Qual é o código da turma que deseja editar? "))
        quem_irei_editar = ler_arquivo_json(nome_arquivo)
        for dicionario in quem_irei_editar:
            if dicionario["Código da turma"] == codigo_de_edicao:
                turma_para_editar = dicionario
                break
        if turma_para_editar is None:
            print("Não foi possivel localizar um professor com esse código")
        else:
            novo_professor = int(input("Digite o código do novo professor: "))
            nova_disciplina = input("Digite o código da nova disciplina: ")
            turma_para_editar["Código do professor"] = novo_professor
            turma_para_editar["Código da disciplina"] = nova_disciplina
            salvar_arquivo_json(quem_irei_editar, nome_arquivo)
            print("Turma editada com sucesso! Voltando a pagina anterior.")




def excluir(nome_arquivo, opcao_menu_principal):
    """
        Exclui um aluno existente na lista estudantes ou avisa caso não exista um aluno com o código inserido
        :param nome_arquivo: arquivo json
        """
    localizar_o_que_sera_exluido = "vazio"

    if opcao_menu_principal == "1":
        localizar_o_que_sera_exluido = "Código da disciplina"
    elif opcao_menu_principal == "2":
        localizar_o_que_sera_exluido = "Código aluno"
    elif opcao_menu_principal == "3":
        localizar_o_que_sera_exluido = "Código turma"
    elif opcao_menu_principal == "4":
        localizar_o_que_sera_exluido = "Código do professor"
    elif opcao_menu_principal == "5":
        localizar_o_que_sera_exluido = "Código da turma"

    estudante_para_remover = None
    codigo_de_exclusao = int(input("Qual é o código do registro que deseja excluir? "))
    o_que_sera_excluido = ler_arquivo_json(nome_arquivo)
    for dicionario in o_que_sera_excluido:
        if dicionario[localizar_o_que_sera_exluido] == codigo_de_exclusao:
            estudante_para_remover = dicionario
            break
    if estudante_para_remover is None:
        print(f"Não foi possivel localizar o código {codigo_de_exclusao}")
    else:
        o_que_sera_excluido.remove(estudante_para_remover)
        salvar_arquivo_json(o_que_sera_excluido, nome_arquivo)
        print(f"Registro número {codigo_de_exclusao} excluido com sucesso")


def listar(nome_arquivo):
    """
        Mostra os dados da lista estudantes ou avisa se a lista estiver vazia
        :param nome_arquivo: arquivo json
        """
    o_que_sera_listado = ler_arquivo_json(nome_arquivo)
    if not o_que_sera_listado:
        print("Ainda não existe um registro cadastrados!")
    for elemento in o_que_sera_listado:
        print(elemento)


def salvar_arquivo_json(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False)


def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            lista = json.load(f)
            return lista
    except:
        return []


def processar_submenu_operacoes(operacao, nome_arquivo):
    if operacao == "1":
        cadastrar(nome_arquivo, opcao_principal)
    elif operacao == "2":
        editar(nome_arquivo, opcao_principal)
    elif operacao == "3":
        excluir(nome_arquivo, opcao_principal)
    elif operacao == "4":
        listar(nome_arquivo)
    elif operacao == "5":
        return False
    else:
        print(f"Opção {operacao} invalida!")

    return True


# Arquivos:
arquivo_disciplinas = "disciplinas.json"
arquivo_estudantes = "estudante.json"
arquivo_matriculas = "matriculas.json"
arquivo_professores = "professores.json"
arquivo_turmas = "turmas.json"

# Funcionamento do programa:
while True:
    # Menu
    opcao_principal = mostrar_menu_principal()
    print(f"Você escolheu a opção {opcao_principal}")
    # Submenu disciplinas
    if opcao_principal == "1":
        print(f"---Menu de Disciplinas---")
        while True:
            # Submenu
            operacao = mostrar_submenu()
            print(f"Você escolheu a opção {operacao}")
            if not processar_submenu_operacoes(operacao, arquivo_disciplinas):
                break
    # Submenu estudantes
    elif opcao_principal == "2":
        print(f"---Menu de Estudantes---")
        while True:
            # Submenu
            num_operacao = mostrar_submenu()
            print(f"Você escolheu a opção {num_operacao}")
            if not processar_submenu_operacoes(num_operacao, arquivo_estudantes):
                break
    elif opcao_principal == "3":
        print(f"---Menu de Matriculas---")
        while True:
            # Submenu
            operacao = mostrar_submenu()
            print(f"Você escolheu a opção {operacao}")
            if not processar_submenu_operacoes(operacao, arquivo_matriculas):
                break
    elif opcao_principal == "4":
        print(f"---Menu de Professores---")
        while True:
            # Submenu
            operacao = mostrar_submenu()
            print(f"Você escolheu a opção {operacao}")
            if not processar_submenu_operacoes(operacao, arquivo_professores):
                break
    elif opcao_principal == "5":
        print(f"---Menu de Turmas---")
        while True:
            # Submenu
            operacao = mostrar_submenu()
            print(f"Você escolheu a opção {operacao}")
            if not processar_submenu_operacoes(operacao, arquivo_turmas):
                break
        # Menu principal = 0 sair
    elif opcao_principal == "0":
        break
    # Mensagem opção invalida do menu principal
    else:
        print(f"Opção {opcao_principal} invalida!")