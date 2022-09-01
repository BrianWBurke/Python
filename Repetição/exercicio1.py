# Melhorando calculadora da aula 3

print('CALCULADORA')
print('Qual operação deseja fazer?')
print('+')
print('-')
print('*')
print('/')
print('Ou digite "s" para sair')

while True:
  op = input('Qual operação deseja fazer? ')

  if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite um valor inteiro: '))
    y = int(input('Digite outro valor inteiro: '))
  if(op == '+'):
      res = x + y
      print(f'{x} {op} {y} = {res}')
      continue
  elif(op == '-'):
      res = x - y
      print(f'{x} {op} {y} = {res}')
      continue
  elif(op == '*'):
      res = x * y
      print(f'{x} {op} {y} = {res}')
      continue
  elif(op == '/'):
      res = x / y
      print(f'{x} {op} {y} = {res}')
      continue
  elif(op == 's'):
      break
  else:
      print('operação inválida, escreva um dos operadores acima')

print('Encerrando a calculadora....')