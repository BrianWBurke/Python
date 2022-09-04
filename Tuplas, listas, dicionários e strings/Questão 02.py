#Apresentação e cardápio
print('Bem vindo a Pizzaria do Brian Willian Burke')
print('--------------------Cardápio-----------------------')
print('| Código | Descrição  | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana |   R$ 20,00  |    R$ 26,00  |')
print('|   22   | Margherita |   R$ 20,00  |    R$ 26,00  |')
print('|   23   | Calabresa  |   R$ 25,00  |    R$ 32,50  |')
print('|   24   | Toscana    |   R$ 30,00  |    R$ 39,00  |')
print('|   25   | Portuguesa |   R$ 30,00  |    R$ 39,00  |')
print('----------------------------------------------------')

preco = 0

#Laço do programa
while True:
    #Verificando tamanho da pizza
    tamanho = input('Qual tamanho de pizza que deseja? (M/G): ')
    if (tamanho != 'M' and tamanho != 'G'):
        print('Opção inválida')
        continue #Retornando ao início

    #Verificando sabores da pizza
    codigo = int(input('Entre com o código do sabor que deseja: '))

    #Condicionais por tamanho e código
    if (codigo == 21 and tamanho == 'M'):
        print('Você pediu de Napolitana (M)')
        preco += 20
    elif (codigo == 21 and tamanho == 'G'):
        print('Você pediu de Napolitana (G)')
        preco += 26
    elif (codigo == 22 and tamanho == 'M'):
        print('Você pediu de Margherita (M)')
        preco += 20
    elif (codigo == 22 and tamanho == 'G'):
        print('Você pediu de Margherita (G)')
        preco += 26
    elif (codigo == 23 and tamanho == 'M'):
        print('Você pediu de Calabresa (M)')
        preco += 25
    elif (codigo == 23 and tamanho == 'G'):
        print('Você pediu de Calabresa (G)')
        preco += 32.50
    elif (codigo == 24 and tamanho == 'M'):
        print('Você pediu de Toscana (M)')
        preco += 30
    elif (codigo == 24 and tamanho == 'G'):
        print('Você pediu de Toscana (M)')
        preco += 39
    elif (codigo == 25 and tamanho == 'M'):
        print('Você pediu de Portuguesa (M)')
        preco += 30
    elif (codigo == 25 and tamanho == 'G'):
        print('Você pediu de Portuguesa (G)')
        preco += 39
    else:
        print('Opção inválida')
        continue #Retornando ao início

    #Verificando se o cliente deseja continuar para mais um pedido
    print('deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    confirma = int(input(''))

    #Condicional para verificar o desejo do cliente
    if confirma == 1:
        continue
    elif confirma == 0:
        print(f'O total a ser pago é: R$ {preco:.2f}')
        break
    else:
        print('código inválido, finalizando o pedido.') #Caso o cliente digite código inválido nessa parte o programa finaliza
        print(f'O total a ser pago é: R$ {preco:.2f}')
        break