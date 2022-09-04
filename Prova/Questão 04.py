listaProdutos = []
#---------- COMEÇO cadastrarProduto ----------
def cadastrarProduto(cod):
    try:
        print('Bem-vindo ao CADASTRAR produto')
        if(cod > 0 and cod < 10):
            print(f'O CÓDIGO do produto a ser cadastrado é: 00{cod}') # Adicionando dois zeros na frente de números de 1 a 9
        elif(cod >= 10 and cod <= 99):
            print(f'O CÓDIGO do produto a ser cadastrado é: 0{cod}')  # Adicionando um zero na frente de números de 10 a 99
        elif (cod >= 100):
            print(f'O CÓDIGO do produto a ser cadastrado é: {cod}')   # Impriminado normalmente para número de 100 para cima
        nomeProd = input('Digite o NOME do produto: ')
        fabricante = input('Digite o FABRICANTE do produto: ')
        valorProd = float(input('Digite o VALOR(R$) do produto: '))
        dicionarioProduto = {'cod'       : cod,
                             'nomeProd'  : nomeProd,
                             'fabricante': fabricante,
                             'valorProd' : valorProd}
        listaProdutos.append(dicionarioProduto.copy())
        return
    except ValueError:
        print('Você não está digitando valores válidos')
#---------- FIM cadastrarProduto ----------

#---------- COMEÇO consultarProduto ----------
def consultarProduto():
    while True:
        try:
            print('Bem-vindo ao CONSULTAR produtos')
            if not listaProdutos: # Caso não tenha produtos cadastrados irá imprimir que não existem produtos cadastrados e voltar.
                print('Sem produtos cadastrados')
                break
            else: # Caso haja produtos cadastrados abre menu de consultar
                opConsultar = int(input('Entre com a opção desejada\n'
                                        '1- Consultar TODOS OS PRODUTOS\n'
                                        '2- Consultar produto por CÓDIGO\n'
                                        '3- Consultar por FABRICANTE\n'
                                        '4- Retornar'
                                        '\n>>'))

                if(opConsultar == 1): # Opção de consultar todos produtos
                    print('Bem-vindo a consultar TODOS OS PRODUTOS')
                    for produto in listaProdutos:
                        for key, value in produto.items():
                            if (key == 'valorProd'): # Caso a opção seja valorProd, adicionar "R$" e duas casas após a virgula
                                print(f'{key} : R$ {value:.2f}')
                            else:
                                print(f'{key} : {value}')
                elif(opConsultar == 2): # Opção de consultar produto por código
                    print('Bem-vindo a consultar CÓDIGO')
                    entrada = int(input('Digite o CÓDIGO desejado: '))
                    for produto in listaProdutos:
                        if(produto['cod'] == entrada):
                            for key, value in produto.items():
                                if (key == 'valorProd'):
                                    print(f'{key} : R$ {value:.2f}')
                                else:
                                    print(f'{key} : {value}')

                elif(opConsultar == 3): # Opção de consultar produto por fabricante
                    print('Bem-vindo a consultar FABRICANTE')
                    entrada = input('Digite o FABRICANTE desejada: ')
                    for produto in listaProdutos:
                        if(produto['fabricante'] == entrada):
                            for key, value in produto.items():
                                if (key == 'valorProd'):
                                    print(f'{key} : R$ {value:.2f}')
                                else:
                                    print(f'{key} : {value}')
                elif(opConsultar == 4): # Retornar ao menu principal
                    print('Retornando')
                    return
                else:
                    print('Você digitou uma opção que não existe')
                    continue
        except ValueError:
            print('Você não está digitando valores inteiros')
#---------- FIM consultarProduto ----------

#---------- COMEÇO removerProduto ----------
def removerProduto():
    try:
        print('Bem-vindo ao REMOVER produtos')
        if not listaProdutos: # Caso não tenha produtos cadastrados irá imprimir que não existem produtos cadastrados e voltar.
            print('Sem produtos cadastrados para remover')
        else: # Caso contrario abre menu
            entrada = int(input('Digite o CÓDIGO do produto que deseja REMOVER: '))
            for produto in listaProdutos:
                if(produto['cod'] == entrada):
                    print(f'O produto {produto["nomeProd"]} com código {produto["cod"]} foi removido')
                    listaProdutos.remove(produto)
    except ValueError:
        print('Você não está digitando valores inteiros')
#---------- FIM removerProduto ----------

#---------- COMEÇO MAIN ----------
print('Bem-vindo ao programa Controle de Estoque de Produtos da Mercearia Brian Willian Burke')
codProd = 0
while True:
    try:
        # Menu principal
        opcao = int(input('Digite a opção desejada:\n'
                        '1- Cadastrar Produto\n'
                        '2- Consultar Produto\n'
                        '3- Remover Produto\n'
                        '4- Sair'
                        '\n>>'))
        if(opcao == 1):
            codProd += 1
            cadastrarProduto(codProd)
        elif(opcao == 2):
            consultarProduto()
        elif(opcao == 3):
            removerProduto()
        elif(opcao == 4):
            print('Programa finalizado')
            break
        else:
            print('Você digitou uma opção que não existe')
            continue
    except ValueError:
        print('Você não está digitando valores inteiros')
#---------- FIM MAIN ----------