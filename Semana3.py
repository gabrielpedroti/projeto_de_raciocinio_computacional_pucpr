# Boas vindas e menu
print("----Seja bem vindo ao menu!----")
print("1 - Disciplinas")
print("2 - Estudantes")
print("3 - Matriculas")
print("4 - Professores")
print("5 - Turmas")
print("0 - Sair")

# Selecionar opção do menu
while True:
    opcao_principal = (input("Digite o número da opção desejada (0 para finalizar): "))
    if opcao_principal == "1" or opcao_principal == "2" or opcao_principal == "3" \
            or opcao_principal == "4" or opcao_principal == "5":
        print(f"Você escolheu a opção {opcao_principal}")
        print(f"---Menu opção número {opcao_principal}---")

        # Submenu
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("5 - Voltar ao menu anterior")

        while True:
            operacao = (input("Digite o número da opção desejada: "))
            if operacao == "1" or operacao == "2" or operacao == "3" \
                    or operacao == "4":
                print(f"Você escolheu a opção {operacao}")
            elif operacao == "5":
                break
            else:
                print(f"Opção {operacao} invalida!")
    # menu principal = 0 sair
    elif opcao_principal == "0":
        break
    # mensagem invalida principal
    else:
        print(f"Opção {opcao_principal} invalida!")
