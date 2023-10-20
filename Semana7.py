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


def cadastrar_aluno(nome_arquivo):
    """
    Adiciona um aluno a lista estudantes
    :param nome_arquivo: arquivo json
    :return:
    """
    codigo = int(input("Digite o codigo do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite cpf do estudante: ")
    dicionario_novo_estudante = {"codigo aluno": codigo, "nome aluno": nome, "cpf aluno": cpf}
    quem_irei_cadastrar = ler_arquivo_json(nome_arquivo)
    quem_irei_cadastrar.append(dicionario_novo_estudante)
    salvar_arquivo_json(quem_irei_cadastrar, nome_arquivo)
    print(f"Aluno(a) {nome} cadastrado(a) com sucesso! Voltando a pagina anterior.")


def editar_aluno(nome_arquivo):
    """
    Edita um aluno existente na lista estudantes ou avisa caso não exista um aluno com o código inserido
    :param nome_arquivo: arquivo json
    """
    estudante_para_editar = None
    codigo_de_edicao = int(input("Qual é o código do aluno que deseja editar? "))
    quem_irei_editar = ler_arquivo_json(nome_arquivo)
    for dicionario_estudantes in quem_irei_editar:
        if dicionario_estudantes["codigo aluno"] == codigo_de_edicao:
            estudante_para_editar = dicionario_estudantes
            break
    if estudante_para_editar is None:
        print("Não foi possivel localizar um aluno com esse código")
    else:
        novo_nome = input("Digite um nome para o estudante: ")
        novo_cpf = input("Digite cpf do estudante: ")
        estudante_para_editar["nome aluno"] = novo_nome
        estudante_para_editar["cpf aluno"] = novo_cpf
        salvar_arquivo_json(quem_irei_editar, nome_arquivo)
        print("Estudante editado com sucesso! Voltando a pagina anterior.")


def excluir(nome_arquivo):
    """
        Exclui um aluno existente na lista estudantes ou avisa caso não exista um aluno com o código inserido
        :param nome_arquivo: arquivo json
        """
    estudante_para_remover = None
    codigo_de_exclusao = int(input("Qual é o código do aluno que deseja excluir? "))
    o_que_sera_excluido = ler_arquivo_json(nome_arquivo)
    for dicionario_estudantes in o_que_sera_excluido:
        if dicionario_estudantes["codigo aluno"] == codigo_de_exclusao:
            estudante_para_remover = dicionario_estudantes
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
        print("Ainda não existe estudantes cadastrados!")
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


# Listas:
arquivo_estudantes = "estudante.json"

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
                cadastrar_aluno(arquivo_estudantes)
            elif operacao == "2":
                editar_aluno(arquivo_estudantes)
            elif operacao == "3":
                excluir(arquivo_estudantes)
            elif operacao == "4":
                listar(arquivo_estudantes)
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

