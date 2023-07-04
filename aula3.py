#Exercícios de Aula - Prática 3

# Exercicio 1 -----------------------------------------------

a = int(input('Digite o 1° lado do triângulo'))
b = int(input('Digite o 2° lado do triângulo'))
c = int(input('Digite o 3° lado do triângulo'))

if (a > 0) and (b > 0) and (c >0):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a != b and a != c and b != c:
            print('Triângulo escaleno!')
        elif a == b and a == c and b == c:
            print('Triângulo esquilátero!')
        else:
            print('Triângulo isóceles!')
    else:
        print('Ao menos um dos valores indicados não servem para a formação de um triângulo!')
else:
    print('Ao menos um dos valores indicados não servem para a formação de um triângulo, os valores precisam ser maior que zero!')

# Exercicio 2 ---------------------------------------------------

print('CALCULADORS')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer tecla para sair')

operacao = input('Qual operação deseja fazer?')
if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))


if (operacao == '+'):
    resposta = x + y
    print('Você escolheu adição e o resultado é {}'.format(resposta))
elif (operacao == '-'):
    resposta = x - y
    print('Você escolheu subtração e o resultado é {}'.format(resposta))
elif (operacao == '*'):
    resposta = x * y
    print('Você escolheu multiplicação e o resultado é {}'.format(resposta))
elif (operacao == '/'):
    resposta = x * y
    print('Você escolheu divisão e o resultado é {}'.format(resposta))
else:
    print('Operção inválida')

print('Encerrando o programa.. ')

# Exercicio 3 ---------------------------------------------------

kwh = float(input('Quantos Kwh?'))
tipo = input('Qual o tipo de instalação (R, C ou I)')

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação inválida!')

print('Total a pagar {}'.format(kwh * preco))