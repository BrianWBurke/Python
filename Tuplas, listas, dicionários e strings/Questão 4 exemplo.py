listaEstudantes = []
#---------- COMEÇO cadastrarEstudante ----------
def cadastrarEstudante(ru):
    print('Bem-vindo ao CADASTRAR estudantes')
    print(f'O RU do estudante a ser cadastrado é: {ru}')
    nome = input('Digite o nome do estudante: ')
    turma = input('Digite o turma do estudante: ')
    dicionarioEstudante = {'ru'   : ru, 
                           'nome' : nome,
                           'turma': turma}
    listaEstudantes.append(dicionarioEstudante.copy())
#---------- FIM cadastrarEstudante ----------

#---------- COMEÇO consultarEstudante ----------
def consultarEstudante():
    while True:
        try:
            print('Bem-vindo ao CONSULTAR estudantes')
            opConsultar = int(input('Entre com a opção desejada\n'
                                    '1- Consultar todos os Estudante\n'
                                    '2- Consultar por RU\n'
                                    '3- Consultar por Turma\n'
                                    '4- Retornar'
                                    '\n>>'))
            if(opConsultar == 1):
                print('Bem-vindo a consultar TODOS OS ESTUDANTES')
                for estudante in listaEstudantes: #selecionar cada dicionario da minha lista (cada estudante da lista de estudantes)
                    for key, value in estudante.items(): #selecionar cada conjunto 'chave' : valor dicionario da minha lista
                        print(f'{key} : {value}')
            elif(opConsultar == 2):
                print('Bem-vindo a consultar RU')
                entrada = int(input('Digite o RU desejado: '))                
                for estudante in listaEstudantes:
                    if(estudante['ru'] == entrada):
                        for key, value in estudante.items():
                            print(f'{key} : {value}')

            elif(opConsultar == 3):
                print('Bem-vindo a consultar TURMA')                
                entrada = input('Digite a TURMA desejada: ')                
                for estudante in listaEstudantes:
                    if(estudante['turma'] == entrada):
                        for key, value in estudante.items():
                            print(f'{key} : {value}')
            elif(opConsultar == 4):
                print('Retornando')
                return
            else:
                print('Você digitou uma opção que não existe')
                continue
        except ValueError:
            print('Você não está digitando valores inteiros')

#---------- FIM consultarEstudante ----------

#---------- COMEÇO removerEstudante ----------
def removerEstudante():
    print('Bem-vindo ao REMOVER estudantes')
    entrada = int(input('Digite a RU do estudante que deseja REMOVER: '))                
    for estudante in listaEstudantes:
        if(estudante['ru'] == entrada):
            listaEstudantes.remove(estudante)
#---------- FIM removerEstudante ----------

#---------- COMEÇO MAIN ----------
print('Bem-vindo ao programa Controle de Estudantes Brian Willian Burke')
registroAcademico = 0
while True:
    try:
        opcao = int(input('Digite a opção desejada:\n'
                        '1- Cadastrar Estudante\n'
                        '2- Consultar Estudante\n'
                        '3- Remover estudante\n'
                        '4- Sair'
                        '\n>>'))
        if(opcao == 1):
            registroAcademico += 1
            cadastrarEstudante(registroAcademico)
        elif(opcao == 2):
            consultarEstudante()
        elif(opcao == 3):
            removerEstudante()
        elif(opcao == 4):
            print('Programa finalizado')
            break
        else:
            print('Você digitou uma opção que não existe')
            continue
    except ValueError:
        print('Você não está digitando valores inteiros')
#---------- FIM MAIN ----------
