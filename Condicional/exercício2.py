print('Olá, seja bem vindo ao hortifruti! Escolha o que deseja comprar: ')
print('Por favor digite o número correspondente do seu pedido:')
print('1-Maça (R$2,30)')
print('2-Laranja (R$3,60)')
print('3-Banana (R$1,85)')
fruta = int(input('Sua escolha é: '))

if (fruta < 1 or fruta > 3):
    print('Produto inexistente!')
else:    
    qnt = int(input('Por favor, digite a quantidade que desejada: '))

if (fruta == 1):
    total = qnt * 2.3
    print(f'Você comprou {qnt} maça(s). Total à pagar: R$ {total:.2f}')
else:
    if (fruta == 2):
        total = qnt * 3.6
        print(f'Você comprou {qnt} laranja(s). Total à pagar: R$ {total:.2f}')
    else:
        if (fruta == 3):
            total = qnt * 1.85
            print(f'Você comprou {qnt} banana(s). Total à pagar: R$ {total:.2f}')