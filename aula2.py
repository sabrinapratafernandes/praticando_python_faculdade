# Exercicio ---------------------------------------------------------

preco = float(input('Digite o preço do produto'))
pdesconto = float(input('Digite o percentual de desconto'))

desconto = preco * (pdesconto / 100)
preco_final = preco - desconto

print(' O preço do produto é {}. Desconto de {}%'.format(preco, pdesconto))
print("Valor calculado de desconto: {}. Valor final do produto: {}".format(desconto, preco_final))

# Exercicio 2 ----------------------------------------------------

km = int(input('Quantos km foram percorridos?'))
dias = int(input('Por quantos dias o carro foi alugado?'))

preco2 = 60 * dias + 0.15 * km
print('Km = {}. Dias {}'. format(km, dias))
print('Valor a ser pago: {}'.format(preco2))

# Exercicio 3 ----------------------------------------------------

frase = input('Digite uma frase')
tamanho = len(frase)

pedaco_frase = frase[:int(tamanho/2)]
print(pedaco_frase[-2:])