# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto. 

preco = float(input('Digite o preço do produto '))
percentual = int(input('digite o percentual de desconto (0-100)% '))

valorD = round(preco * (percentual / 100), 2)

valorF = round(preco - valorD, 2)

print(f'O preço do produto é R$ {preco:.2f}. Desconto de {percentual}%')
print(f'O valor do desconto é R$ {valorD:.2f} | O valor final do produto é de: R$ {valorF:.2f}')