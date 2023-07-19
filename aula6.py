# Importando bibliotecas

# import math as n = Importa toda a biblioteca
from math import sqrt # Importa a função desejada

print(sqrt(9))

# Exercicios

# Tuplas: ()
# Listas: []
# Dicionários: {}

# Crie uma lista de notas e conte a quantidade de vezes que uma nota é apresentada
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))

# Crie uma tupla com 5 palavras, encontre as vogais de cada palavra e faça um print com o nome da palavra e suas respectivas vogais
palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='  ')

# Crie um jogo de pedra papel e tesoura para jogar contra o computador que irá sortear um número de 1 até 3 para jogar, apresente todos os resultados em uma lista e no final apresente ao vencedor

import random
def valida_int(pergunta, min, max): # Recebe o dado via parâmetros
    x = int(input(pergunta))
    while ((x < min) or (x > max)): # Verifica se o dado obedece os parâetros definidos
        x = int(input(pergunta)) # transforma o dado em um inteiro
    return x # Retorna o valor definido

def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1: #Pedra
        if jogador2 == 1:  # Pedra
            empate += 1
        elif jogador2 == 2:  # Papel
            v2 += 1
        elif jogador2 == 3:  # Tesoura
            v1 += 1
    elif jogador1 == 2: #Papel
        if jogador2 == 1:  # Pedra
            v1 += 1
        elif jogador2 == 2:  # Papel
            empate += 1
        elif jogador2 == 3:  # Tesoura
            v2 += 1
    elif jogador1 == 3: #Tesoura
        if jogador2 == 1:  # Pedra
            v2 += 1
        elif jogador2 == 2:  # Papel
            v1 += 1
        elif jogador2 == 3:  # Tesoura
            empate += 1
    resultados = [v1, v2, empate]
    return resultados

print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('Para encerrar digite 0')

resultados  = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    jogada1 = valida_int('Escolha sua jogada', 0, 3) # Chama a função de verificação do dado e conversão para um inteiro,passando o dado recebido
    if jogada1 == 0: # Verifica se a opção de encerrar o programa foi selecionada e encerra no break se sim
        break
    jogada2 = random.randint(1,3) # Computador gera um número aleatório dentre a margem passada invocando a biblioteca random importada anteriormente
    jogadas.append([jogada1, jogada2]) # Armazena a informação das jogadas de cada jogador por jogo
    resultados = vencedor(jogada1, jogada2)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end=' ')
        print()

print('Número de vitórias do Jogador 1: {}'.format(resultados[0]))
print('Número de vitórias do Jogador 2: {}'.format(resultados[1]))
print('Número de empates: {}'.format(resultados[2]))


