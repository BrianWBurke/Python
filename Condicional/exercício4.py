# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição(+), subtração(-), multiplucação(*) ou divisão(/). Exiba na tela o resultado da operação desejada.
print('CALCULADORA')
print('Qual operação deseja fazer?')
print('+')
print('-')
print('*')
print('/')

op = input('Escolha uma das opções acima: ')
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite outro valor inteiro: '))

if(op == '+'):
    res = x + y
elif(op == '-'):
    res = x - y
elif(op == '*'):
    res = x * y
elif(op == '/'):
    res = x / y
else:
    print('operação inválida, escreva um dos operadores acima')

print(f'{x} {op} {y} = {res}')