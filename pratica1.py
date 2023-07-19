print('Bem-vindo a loja da Sabrina Bueno Prata Fernandes!')

valor = float(input('Entre com o valor do produto:'))
quantidade = int(input('Entre com a quantidade do produto:'))

if (quantidade >= 2000): # Verifica se a quantidade é maior ou igual a 2000
    desconto = 0.15  # Desconto de 15%
    total_sem_desconto = valor * quantidade
    valor_desconto = total_sem_desconto * desconto
    total_com_desconto = total_sem_desconto - valor_desconto
    print('O valor SEM desconto: R$ {}'.format(total_sem_desconto))
    print('O valor COM desconto: R$ {}'.format(total_com_desconto))
elif (quantidade >= 1000) and (quantidade < 2000): # Verifica se a quantidade é maior ou igual a 1000 e menor 2000
    desconto = 0.1  # Desconto de 10%
    total_sem_desconto = valor * quantidade
    valor_desconto = total_sem_desconto * desconto
    total_com_desconto = total_sem_desconto - valor_desconto
    print('O valor SEM desconto: R$ {}'.format(total_sem_desconto))
    print('O valor COM desconto: R$ {}'.format(total_com_desconto))
elif (quantidade >= 200) and (quantidade < 1000): # Verifica se a quantidade é maior ou igual a 200 e menor que 1000
    desconto = 0.05  # Desconto de 5%
    total_sem_desconto = valor * quantidade
    valor_desconto = total_sem_desconto * desconto
    total_com_desconto = total_sem_desconto - valor_desconto
    print('O valor SEM desconto: R$ {}'.format(total_sem_desconto))
    print('O valor COM desconto: R$ {}'.format(total_com_desconto))
else: # Verifica se a quantidade é menor que 200
   preco = valor * quantidade
   print('Seu pedido não possui desconto pois a quantidade de produtos é inferior a 200!')
   print('O valor é de: R$ {}'.format(preco))










