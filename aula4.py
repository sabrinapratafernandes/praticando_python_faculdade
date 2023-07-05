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

# Exercicio 4:

valor = int(input('Digite o valor em R$'))

while True:
    if valor >= 100:
        cedulas100 = valor // 100
        valor -= cedulas100 * 100
        print('Cédulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50
        valor -= cedulas50 * 50
        print('Cédulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor // 20
        valor -= cedulas20 * 20
        print('Cédulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10
        valor -= cedulas10 * 10
        print('Cédulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor -= cedulas5 * 5
        print('Cédulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if valor:
        cedulas1 = valor
        print('Cédulas de 1: {}'.format(cedulas1))
        break

# Exercicio 3:

total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade? (Para resultado digite calcular!)')
    if idade =='calcular':
        break
    idade = int(idade)
    total += 1

    if idade < 3:
        ingresso = 0
    elif idade > 12:
        ingresso = 30
    else:
        ingresso = 15

    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado {}'.format(dinheiro))
print('Média arrecadada {}'.format(media))