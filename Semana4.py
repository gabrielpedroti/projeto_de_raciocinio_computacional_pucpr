# Listas
estudantes = []

while True:
    # Menu
    print("----MENU PRINCIPAL!----")
    print("1 - Disciplinas")
    print("2 - Estudantes")
    print("3 - Matriculas")
    print("4 - Professores")
    print("5 - Turmas")
    print("0 - Sair")

    opcao_principal = (input("Digite o número da opção desejada (0 para finalizar): "))
    print(f"Você escolheu a opção {opcao_principal}")

    # Opções em desenvolvimento
    if opcao_principal == "1" or opcao_principal == "3" or opcao_principal == "4" or opcao_principal == "5":
        print("!EM DESENVOLVIMENTO!")
    # Submenu estudantes
    elif opcao_principal == "2":
        print(f"---Menu de Estudantes---")

        while True:
            # Submenu
            print("1 - Cadastrar")
            print("2 - Editar")
            print("3 - Excluir")
            print("4 - Listar")
            print("5 - Voltar ao menu anterior")

            operacao = input("Digite o número da opção desejada: ")
            print(f"Você escolheu a opção {operacao}")

            if operacao == "1":
                novo_estudante = str(input("Digite o nome do estudante: "))
                estudantes.append(novo_estudante)
                print("Novo estudante cadastrado com sucesso! Voltando a pagina anterior.")
            elif operacao == "2" or operacao == "3":
                print("!EM DESENVOLVIMENTO!")
            elif operacao == "4":
                if not estudantes:
                    print("Ainda não existe estudantes cadastrados!")
                for elemento in estudantes:
                    print(elemento)
            elif operacao == "5":
                break
            else:
                print(f"Opção {operacao} invalida!")

    # Menu principal = 0 sair
    elif opcao_principal == "0":
        break
    # mensagem invalida principal
    else:
        print(f"Opção {opcao_principal} invalida!")