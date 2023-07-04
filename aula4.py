# Exercicios de aula prática 4

# Laços de repetição - utilizando while e for
# operadores especiais de atribuição

# Exercício 1:
print('Imprimir de 3 a 12 utilizando o for')
for i in range(3,13,1):
    print(i)

# Exercício 2:
print('Imprimir de 3 a 12 utilizando o while')
i2 = 3
while (i2 < 13):
    print(i2)
    i2 = i2 + 1

# Exercicio 3: (Utilizando a calculadora da aula anterior)
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione s para sair')

while True:
    operacao = input('Qual operação deseja fazer?')
    if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))

    if (operacao == '+'):
        resposta = x + y
        print('Você escolheu adição e o resultado é {}'.format(resposta))
        continue
    elif (operacao == '-'):
        resposta = x - y
        print('Você escolheu subtração e o resultado é {}'.format(resposta))
        continue
    elif (operacao == '*'):
        resposta = x * y
        print('Você escolheu multiplicação e o resultado é {}'.format(resposta))
        continue
    elif (operacao == '/'):
        resposta = x / y
        print('Você escolheu divisão e o resultado é {}'.format(resposta))
        continue
    elif (operacao == 's'):
        break
    else:
        print('Operação inválida')
print('Encerrando o programa.. ')


