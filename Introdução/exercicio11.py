# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

km = int(input('Informe os kms percorridos: '))
dias = int(input('Informa a quantidade de dia: '))

preco = dias * 60 + km * 0.15

print(f'km rodado: {km} | qtd de dias: {dias} | Total a pagar: R$ {preco:.2f}')