print('Seja bem vindo ao Atacadista do Brian Willian Burke!')
valorP = float(input('Por gentileza, entre com o valor do produto: '))

if (valorP >= 0):
    qnt = int(input('Por gentileza, entre com a quantidade do produto: '))
    if (qnt >= 0):
        if (qnt >= 0 and qnt <= 4):
            total = qnt * valorP
            print(f'O valor sem desconto é: R$ {total:.2f}')
            print(f'O valor com desconto é: R$ {total:.2f}')
        elif (qnt >= 5 and qnt <= 19):
            desc = 3 / 100
            totalS = qnt * valorP
            totalD = totalS * desc
            totalF = totalS - totalD
            print(f'O valor sem desconto é: R$ {totalS:.2f}')
            print(f'O valor com desconto é: R$ {totalF:.2f}  (desconto de 3%)')
        elif (qnt >= 20 and qnt <= 99):
            desc = 6 / 100
            totalS = qnt * valorP
            totalD = totalS * desc
            totalF = totalS - totalD
            print(f'O valor sem desconto é: R$ {totalS:.2f}')
            print(f'O valor com desconto é: R$ {totalF:.2f}  (desconto de 6%)')
        elif (qnt >= 100):
            desc = 10 / 100
            totalS = qnt * valorP
            totalD = totalS * desc
            totalF = totalS - totalD
            print(f'O valor sem desconto é: R$ {totalS:.2f}')
            print(f'O valor com desconto é: R$ {totalF:.2f}  (desconto de 10%)')
    else:
        print('Valor digitado é inválido')
else:
    print('Valor digitado é inválido')
