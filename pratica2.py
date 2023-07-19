import math

print('Bem vindo(a) a sorveteria da Sabrina Bueno Prata Fernandes')

# Definição das linhas para exibir o cardápio
linhas = [
    ['N° DE BOLAS', 'Sabor Tradicional (tr)', 'Sabor premium (pr)', 'Sabor especial (es)'],
    ['1', 'R$ 6,00', 'R$ 7,00', 'R$ 8,00'],
    ['2', 'R$ 10,00', 'R$ 12,00', 'R$ 14,00'],
    ['3', 'R$ 14,00', 'R$ 17,00', 'R$ 20,00']
]

# Função para imprimir o menu
def print_menu():
    # Itera sobre as linhas do cardápio
    for numero_linha, linha in enumerate(linhas):
        texto_linha = '|'

        # Itera sobre as colunas de cada linha
        for numero_coluna, coluna in enumerate(linha):
            tamanho_coluna = len(' {} '.format(linhas[0][numero_coluna]))
            lados = 1

            # Calcula a quantidade de espaços adicionais para centralizar o texto na coluna
            metade_coluna = math.ceil(len(coluna) / 2)

            if numero_linha > 0:
                metade = math.floor(tamanho_coluna / 2)
                lados = metade - metade_coluna

            # Adiciona os espaços adicionais nos lados do texto
            coluna = (lados * ' ' + coluna + lados * ' ')

            # Completa a coluna com espaços em branco, se necessário
            while len(coluna) < tamanho_coluna:
                coluna += ' '

            texto_linha += coluna
            texto_linha += '|'

        # Cria a Linha inicial do cardapio
        if numero_linha == 0:
            tamanho_linha = len(texto_linha)
            metade = math.floor(tamanho_linha / 2)
            fechar = (metade - 4) * '-' + 'Cardápio'
            while len(fechar) < tamanho_linha:
                fechar += '-'
            print(fechar)

        # Imprime a linha atual
        print(texto_linha)

        # Cria a Linha final do cardapio
        if len(linhas) - 1 == numero_linha:
            print(tamanho_linha * '-')

# Chama a função para imprimir o menu
print_menu()

while True:
    # Solicita ao usuário que digite o sabor desejado
    sabor = input("Digite o sabor desejado (tr - Tradicional, es - Especial, pr - Premium): ")

    # Verifica se o sabor digitado é válido (tr, es, pr)
    if sabor not in ['tr', 'es', 'pr']:
        # Sabor inválido, exibe uma mensagem de erro e retorna ao início do loop
        print("Sabor inválido. Por favor, digite tr, es ou pr.")
        continue
    # Solicita ao usuário que digite o número de bolas
    num_bolas = input("Digite o número de bolas (1, 2 ou 3): ")

    # Verifica se o número de bolas digitado é válido (1, 2, 3)
    if num_bolas not in ['1', '2', '3']:

        # Número de bolas inválido, exibe uma mensagem de erro e retorna ao início do loop
        print("Número de bolas inválido. Por favor, digite 1, 2 ou 3.")
        continue

    # Imprime as opções selecionadas pelo usuário
    print("Você pediu {} bolas de sorvete no sabor {}".format(num_bolas,sabor))

    # Pergunta ao usuário se deseja fazer mais um pedido
    continuar = input("Deseja fazer mais um pedido? (s - Sim, n - Não): ")

    # Usuário não deseja fazer mais um pedido, encerra o loop
    if continuar == 'n':
        break


