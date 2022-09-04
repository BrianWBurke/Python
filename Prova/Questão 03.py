#Confirmação e cálculo do valor por volume da feijoada
def volumeFeijoada(pergunta):
    try:
        x = int(input(pergunta))
        if (x < 300 or x > 5000):
            print('Não vendemos menos de 300ml e mais de 5l. Tente novamente!')
            return True
        else:
            volume = x * 0.08
        return float(volume)
    except:
        print('Houve algum erro, por favor tente novamente.')
        return True

#Confirmação e cálculo do valor da opção de feijoada
def opcaoFeijoada(pergunta):
    valor = 0
    while True:
        x = input(pergunta)
        if(x == 'b'):
            valor = 1.00
            return valor
        elif(x == 'p'):
            valor = 1.25
            return valor
        elif(x == 's'):
            valor = 1.5
            return valor
        else:
            print('Você não digitou uma opção válida. Tente novamente')
            continue

#Confirmação e cálculo do valor por acompanhamento da feijoada
def acompanhamentoFeijoada(pergunta):
    valor = 0
    while True:
        try:
            x = int(input(pergunta))
            if(x < 0 or x > 4):
                print('Você não digitou uma opção válida. Tente novamente')
                continue
            else:
                if(x == 0):
                    return float(valor)
                elif(x == 1):
                    valor += 5.00
                    continue
                elif (x == 2):
                    valor += 6.00
                    continue
                elif (x == 3):
                    valor += 7.00
                    continue
                else:
                    valor += 3.00
                    continue
        except:
            print('Houve um erro. Por favor digite uma opção válida')
            continue


#Programa principal
print('Bem-vindo ao Lar da Feijoada do Brian Willian Burke')

#laço de repetição do programa principal
while True:
    #Volume da Feijoada
    print('-------MENU VOLUME FEIJOADA-------')
    volume = volumeFeijoada('Escolha a quantidade desejada: ')
    if (volume == True):
        continue

    #Opção da feijoada
    opcao = opcaoFeijoada('-------MENU OPÇÃO FEIJOADA------- \n'
                          'b - Básica (feijão + paiol + costelinha) \n'
                          'p - Premium (feijão + paiol + costelinha + partes de porco) \n'
                          's - Suprema (feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon) \n'
                          '>>  ')

    #Adicionais da feijoada
    adicionais = acompanhamentoFeijoada('Deseja mais algum acompanhamento? \n'
                                        '0 - Encerrar pedido\n'
                                        '1 - 200g de arroz\n'
                                        '2 - 150g de farofa especial\n'
                                        '3 - 100g de couve cozida\n'
                                        '4 - 1 laranja descascada\n'
                                        '>> ')

    #Cálculo do valor final
    total = (volume * opcao) + adicionais

    #Mostrando para o usuário os valores separados e o valor final da compra
    print(f'volume = R$ {volume:.2f} * opção = R$ {opcao:.2f} + adicionais R$ = {adicionais:.2f} - TOTAL A PAGAR: R$ {total:.2f} ')

    #fim do laço de repetição do programa principal
    break