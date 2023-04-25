print("Menu:")
print("1. Cadastrar conta")
print("2. Solicitar financiamento")

# Pede ao usuario escolher
escolha = input("Digite sua escolha (1 ou 2): ")

# Executa o programa escolhido
if escolha == "1":
    # Solicita informações do usuario
  nome = input("Digite seu nome: ")
  idade = input("Digite sua idade: ")
  telefone = input("Digite seu telefone: ")
  cpf = input("Digite seu CPF: ")
  tipo_conta = input("Digite o tipo de conta (basica, premium ou platinum): ")
  tipo_confirmacao = input("Digite o tipo de confirmacao (facial ou biometrica): ")
  
  # verifica se a conta ja existe
  with open("banco.txt", "r") as arquivo:
      conteudo = arquivo.read()
      if cpf in conteudo:
          print("Conta ja cadastrada!")
      else:
          # Adiciona em string as inforamcoes
          informacoes = f"Nome: {nome}\nIdade: {idade}\nTelefone: {telefone}\nCPF: {cpf}\nTipo de conta: {tipo_conta}\nConfirmacao: {tipo_confirmacao}\n"
  
          # Salva as informacoes em um arquivo de texto chamado "banco.txt"
          with open("banco.txt", "a") as arquivo:
              arquivo.write(informacoes)
  
          # Confirma ao usuario que as informacoes foram salvas
          print("A sua conta foi criada!")
        
# Executa o programa escolhido        
elif escolha == "2":
   # Solicita informações do usuario
  cpf = input("Digite seu CPF: ")
  
# verifica se a conta ja existe e esta apta
  with open("banco.txt", "r") as arquivo:
      conteudo = arquivo.read()
      if cpf in conteudo:
          print("Financiamento aprovado!")
      else:
        print("Financiamento reprovado!")

# Retorna erro se a resposta do usuario nao for 1 ou 2
else:
    print("Escolha inválida. Por favor, digite 1 ou 2.")
