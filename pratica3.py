print('Bem vindo(a) ao petshop da Sabrina Bueno Prata Fernandes!')

#Função que recebe o valor do peso do cachorro e retorna o preço correspondente
def cachorro_peso():
    # Loop que recebe o input de valor do peso
    while True:
        try:
            peso = float(input("Entre com o peso do cachorro: ")) # Input
            if (peso < 3): #Confere se o peso é menor que 3 para retornar o valor correspondente
                return 40.00
            elif (peso >= 3) and (peso < 10): #Confere se o peso é maior ou igual a 3 e menor que 10 para retornar o valor correspondente
                return 50.00
            elif (peso >= 10) and (peso < 30): #Confere se o peso é maior ou igual a 10 e menor que 30 para retornar o valor correspondente
                return 60.00
            elif (peso >= 30) and (peso <= 50): #Confere se o peso é maior ou igual a 30 e menor que 50 para retornar o valor correspondente
                return 70.00
            else:
                print("Peso inválido. Digite um valor menor que 50 kg.") #Retorno caso o valor inserido seja maior que 50
        except ValueError:
            print("Valor inválido. Digite um valor numérico.") #Retorno caso o valor inserido não see numérico

#Atribuição do valor calculado a partir do peso na função a base
base = cachorro_peso()

#Função que calcula o multiplicador do valor base conforme pelagem
def cachorro_pelo():
    #Loop que recebe a informação da pelagem e retorna multiplicador
    while True:
        #Opções de multiplicadores apresentadas ao usuário em menu
        print('Entre com o pelo do cachorro')
        print('c - Pelo Curto')
        print('m - Pelo Médio')
        print('l - Pelo Longo')
        pelo = input("Digite a letra referente a opção desejada:")
        if pelo == 'c': #Confere se o pelo é curto
            return 1
        elif pelo == 'm': #Confere se o pelo é médio
            return 1.5
        elif pelo == 'l': #Confere se o pelo é longo
            return 2
        else:
            print("Opção inválida. Digite 'c' para pelo curto, 'm' para pelo médio ou 'l' para pelo longo.")

#Atribuição do valor calculado na função ao multiplicador
multiplicador = cachorro_pelo()

#Função que recebe as opções de serviçoes adicionais e calcula valor extra
def cachorro_extra():
    valor_extra = 0 #Atribui zero como base ao valor extra
    #Loop que recebe o valor correspondente ao serviço adicional
    while True:
        try:
            #Menu apresentado ao usuário
            print('Deseja adicionar mais algum serviço?')
            print('1 - Corte de Unhas - R$ 10,00')
            print('2 - Escovar os Dentes - R$ 12,00')
            print('3 - Limpeza de Orelhas - R$ 15,00')
            print('0 - Não desejo mais nada')
            adicional = int(input("Escolha um serviço adicional:")) #Recebe a opção de serviço adicional
            if adicional == 1: #Confere se o serviço adicional é igual a opção 1 do menu
                valor_extra += 10 #Atribui o valor do serviço a valor_extra se a opção 1 foi a selecionada
            elif adicional == 2: #Confere se o serviço adicional é igual a opção 2 do menu
                valor_extra += 12 #Atribui o valor do serviço a valor_extra se a opção 2 foi a selecionada
            elif adicional == 3: #Confere se o serviço adicional é igual a opção 3 do menu
                valor_extra += 15 #Atribui o valor do serviço a valor_extra se a opção 3 foi a selecionada
            elif adicional == 0: #Verifica se a opção é igual a 0 e encerra o loop se sim
                return valor_extra
            else:
                print("Opção inválida; digite algum dos números do menu. (1,2,3 ou 0)")
        except ValueError:
            print("Opção inválida. Digite um número válido, demais caracteres não são aceitos.")

extra = cachorro_extra()

#Calculo do valor total com base nas variáveis calculadas em cada função
total = base * multiplicador + extra

#Código opcional que inseri para tornar a saída no console mais legível
bold = "\033[1m"  #Deixa o estilo do texto em negrito
reset = "\033[0m" #Reverte o estilo para o padrão

print(bold + 'Total a Pagar: R$ {}'.format(total) + reset)

print(8*'*','CONFIRA OS VALORES:',8*'*')
print('Preço conforme o peso: R$ {}'.format(base))
print('Multiplicador conforme a pelagem: R$ {}'.format(multiplicador))
print('Preço conforme peso e pelagem: R$ {}'.format(base*multiplicador))
print('Preço dos serviços adicionais: R$ {}'.format(extra))
print(bold + 'TOTAL: R$ {}'.format(total) + reset)