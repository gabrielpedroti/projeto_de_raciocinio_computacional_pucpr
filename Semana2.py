#Boas vindas e menu
print("----Seja bem vindo ao menu!----")
print("1 - Disciplinas")
print("2 - Estudantes")
print("3 - Matriculas")
print("4 - Professores")
print("5 - Turmas")
print("0 - Sair")

#Selecionar opção do menu
opcao = int(input("Digite o número da opção desejada: "))
print(f"Você escolheu a opção {opcao}")
if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
  print(f"Menu opção número {opcao}")
elif opcao == 0:
  print("Obrigado por usar o sistema!")
else:
  print("Opção invalida, tente novamente!")
  opcao = int(input("Digite o somente o NÚMERO da opção desejada: "))
  print(f"Você escolheu a opção {opcao}")

#Submenu
print("1 - Cadastrar")
print("2 - Editar")
print("3 - Excluir")
print("4 - Listar")
print("0 - Voltar ao menu anterior")

opcao2 = int(input("Digite o número da opção desejada: "))
print(f"Você escolheu a opção {opcao2}")

