# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# a)Equilátero (três lados iguais) | b)Isósceles (dois lados iguais) | c)Escaleno (três lados diferentes)
# lembrando que para formar um triângulo nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois.

v1 = int(input('Digite o primeiro valor do triângulo: '))
v2 = int(input('Digite o segundo valor do triângulo: '))
v3 = int(input('Digite o terceiro valor do triângulo: '))

if (v1 > 0) and (v2 > 0) and (v3 > 0):  
    if (v1 + v2 > v3) and (v1 + v3 > v2) and (v2 + v3 > v1):
        # Se chegou até aqui, significa que os lados digitados são validos
        if (v1 != v2 and v1 != v3 and v2 != v3):
            print('Triângulo Escaleno (três lados diferentes)')
        else:
            if v1 == v2 and v1 == v3 and v2 == v3: 
                print('Triângulo Equilátero (três lados iguais)')
            else:
                print('Triângulo Isósceles (dois lados iguais')         
    else:
        print('Valor de um dos lados não pode ser maior que a soma dos outros dois')        
else:    
    print('Valor de todos os lados precisa ser diferente de 0')
