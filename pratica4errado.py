print('Bem vindo(a) ao controle de colaboradores da Sabrina Bueno Prata Fernandes!')

lista_colaboradores = []
id_global = 0

#Função que verifica se o dado inserido da opção selecionada no menu é válido
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#Foi necessário criar uma função
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo): # ALTERAR
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'colaboradores'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print(80 * '*')
    print(31 * '-', ' MENU PRINCIPAL ', 31 * '-')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar colaborador')
    print('2 - Consultar Colaborador(es)')
    print('3 - Remover Colaborador')
    print('4 - Sair')

    op = valida_int('Escolha a opção deseada:', 1, 3)
    if op == 1:

    elif op == 2:

    elif op == 3:

    elif op == 4:
        print('Encerrando o programa...')
        break



def cadastrar_colaborador(id):
    global id_global
    while True:
        print('Id do colaborador {}'.format(id_global))
        nome = input("Por favor, digite o Nome do colaborador:")
        setor = input("Por favor, digite o Setor do colaborador: ")
        salario = float(input("Por favor, digite o Salário do colaborador: "))
        colaborador = {
            'id': id,
            'nome': nome,
            'setor': setor,
            'salario': salario
        }

        lista_colaboradores.append(colaborador)
        id_global += 1
        if nome == 'sair':
            print('Encerrando o programa')
            break



def consultar_colaborador():
    while True:
        print("CONSULTAR COLABORADOR")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao Menu")

        opcao = input("Digite sua opção: ")

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

def consultar_todos():
    if len(lista_colaboradores) == 0:
        print("Não há colaboradores cadastrados.")
    else:
        print("Colaboradores cadastrados:")
        for colaborador in lista_colaboradores:
            print(f"ID: {colaborador['id']}, Nome: {colaborador['nome']}, Setor: {colaborador['setor']}, Salário: {colaborador['salario']}")

def consultar_por_id():
    id_colaborador = int(input("Digite o ID do colaborador: "))
    encontrado = False
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_colaborador:
            print(f"Dados do colaborador com ID {id_colaborador}:")
            print(f"Nome: {colaborador['nome']}, Setor: {colaborador['setor']}, Salário: {colaborador['salario']}")
            encontrado = True
            break
    if not encontrado:
        print(f"Colaborador com ID {id_colaborador} não encontrado.")

def consultar_por_setor():
    setor_colaborador = input("Digite o setor do colaborador: ")
    encontrados = False
    for colaborador in lista_colaboradores:
        if colaborador['setor'] == setor_colaborador:
            print(f"Dados do colaborador no setor {setor_colaborador}:")
            print(f"ID: {colaborador['id']}, Nome: {colaborador['nome']}, Salário: {colaborador['salario']}")
            encontrados = True
    if not encontrados:
        print(f"Nenhum colaborador encontrado no setor {setor_colaborador}.")



opcao = int(input('Digite sua opção:'))

while True:
    if opcao == 1:
        cadastrar_colaborador(id)
    elif opcao == 2:
        consultar_colaborador()
    elif opcao == 3:
        remover_colaborador()
    elif opcao == 4:
        print('Encerrando o Programa...')
        break
    else:
        print('Opção inválida, digite novamente conforme numeração das opções.')



