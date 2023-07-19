print('Bem vindo(a) ao controle de colaboradores Sabrina Bueno Prata Fernandes!')
id_global = 0 # Definição da variável de id's
lista_colaboradores = [] # Definição da lista onde serão armazenados os colaboradores

# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    global id_global
    print(80 * '*')
    print(25 * '-', ' MENU CADASTRAR COLABORADOR ', 25 * '-')
    print('Id do colaborador {}'.format(id))
    #Inputs dos dados do colaborador sendo cadastrado
    nome = input("Por favor, digite o Nome do colaborador:")
    setor = input("Por favor, digite o Setor do colaborador: ")
    salario = float(input("Por favor, digite o Salário do colaborador: "))
    #Criação de um dicionário que armazena os dados cadastrados
    colaborador = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_colaboradores.append(colaborador)
    id_global += 1

#Função que consulta a lista_colaboradores e retorna o colaborador
def print_colaborador(colaborador):
    print('Id:{}'.format(colaborador["id"]))
    print('nome:{}'.format(colaborador["nome"]))
    print('setor:{}'.format(colaborador["setor"]))
    print('salario:{}'.format(colaborador["salario"]))

#Função que consulta todos os colaboradores cadastrados na lista_colaboradores mostrando cada colaborador ao chamar a função print_colaborador(colaborador)
def consultar_todos():
    global lista_colaboradores
    for colaborador in lista_colaboradores:
        print_colaborador(colaborador)

# Função que consulta os colaboradores fazendo uma busca pelo id correspondente
def consultar_por_id():
    global lista_colaboradores
    id = int(input('Digite o id do colaborador:')) #Recebe o valor do id que deve ser apresentado
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id: #Define que se o id do cadastro for igual ao que deve ser apresentado deve chamar a função print_colaborador(colaborador)
            print_colaborador(colaborador)
            return
    print('Id não encontrado')

# Função que consulta os colaboradores fazendo uma busca pelo setor correspondente
def consultar_por_setor():
    global lista_colaboradores
    setor = input('Digite o setor dos colaboradores:') #Recebe o valor do setor que deve ser apresentado
    vazio = True
    for colaborador in lista_colaboradores:
        if colaborador["setor"] == setor: #Define que se o setor do cadastro for igual ao que deve ser apresentado deve chamar a função print_colaborador(colaborador)
            print_colaborador(colaborador)
            vazio = False
    if vazio:
        print('Setor vazio')

# Função que realiza consulta no cadastro de colaboradores
def consultar_colaborador():
    while True:
        #Menu apresentado ao usuário
        print(80 * '*')
        print(25 * '-', ' MENU CONSULTAR COLABORADOR ', 25 * '-')
        print("CONSULTAR COLABORADOR")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao Menu")
        opcao = input("Digite sua opção: ") #Recebe a opção deseado pelo usuário

        #Verifica a opção recebida e chama a função corresponte
        if opcao == '1':
            consultar_todos()

        elif opcao == '2':
            consultar_por_id()

        elif opcao == '3':
            consultar_por_setor()

        elif opcao == '4':
            break

        else:
            print("Opção inválida.")

#Função que remove o colaborados da lista existente
def remover_colaborador():
    global lista_colaboradores
    print(80 * '*')
    print(26 * '-', ' MENU REMOVER COLABORADOR ', 26 * '-')
    print('Digite o id do colaborador a ser removido')
    id = int(input('id'))

    # Função para verificar se o colaborador deve ser removido
    def check(colaborador):
        return colaborador["id"] != id
    lista_colaboradores = filter(check, lista_colaboradores) #Mantém apenas os colaboradores com id diferente do inserido para remoção através do filter

#Função que apresenta o menu principal
def main_menu():
    global id_global
    while True:
        #Print do menu
        print(80 * '*')
        print(31 * '-', ' MENU PRINCIPAL ', 31 * '-')
        print('Escolha a opção desejada:')
        print('1 - Cadastrar colaborador')
        print('2 - Consultar Colaborador(es)')
        print('3 - Remover Colaborador')
        print('4 - Sair')
        op = int(input('Opção:'))
        #Verifica a opção selecionada e chama a função correspondente
        if op == 1:
            cadastrar_colaborador(id_global+1)
        elif op == 2:
            consultar_colaborador()
        elif op == 3:
            remover_colaborador()
        elif op == 4:
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida, selecione um número correspondente a ação desejada.')

main_menu()
