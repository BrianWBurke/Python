# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# a)Equilátero (três lados iguais) | b)Isósceles (dois lados iguais) | c)Escaleno (três lados diferentes)

v1 = int(input('Digite o primeiro valor do triângulo: '))
v2 = int(input('Digite o segundo valor do triângulo: '))
v3 = int(input('Digite o terceiro valor do triângulo:3 '))

if (v1 == v2 and v2 == v3):
  print('Triângulo Equilátero (três lados iguais)')
elif (v1 == v2 and v2 != v3  or v2 == v3 and v1 != v2 ):
  print('Triângulo Isósceles (dois lados iguais)')
elif (v1 != v2 and v1 != v3 and v2 != v3):
  print('Triângulo Escaleno (três lados diferentes)')