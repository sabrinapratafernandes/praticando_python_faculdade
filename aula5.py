# Exercícios

# Criando uma função com docstring
def soma(x=0, y=0, z=0):
    """
    Função que soma até trêsvalores inteiros
    :param x: Valor inteiro opcional 1
    :param y: Valor inteiro opcional 2
    :param z: Valor inteiro opcional 3
    """
    return x+y+z
print(soma(3,2))
help(soma)

# Exercício 1
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def fatorial(numero):
    """
    Calcula a fatorial do número inserido
    :param numero: Valor inserido
    :return: Fatorial calculado a partir do valor inserido
    """
    fat = 1
    if numero == 0:
        return fat
    for i in range(1,numero+1,1):
        fat *= i
    return fat

x = valida_int('Digite um valor para calcular a fatorial:', 0, 99999)
print('{}! = {}'.format(x, fatorial(x)))

# Exercicio 2

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

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção deseada:', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo:')
        nomeVideogame = input('Nome do videogame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break