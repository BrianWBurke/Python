# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústria e C para comércios

print('Bem vindo ao calculador de consumo kWh!')
print('Por favor informe seu tipo de instalação: ')
print('Para residência digite R,')
print('Para indústria digite I,')
print('Para comércio digite C.')
inst = input('Digite: ')

if(inst == 'R' or inst == 'I' or inst == 'C'):

    kwh = int(input('Digite o kWh gasto: '))

    if(inst == 'R'):
        if(kwh > 0 and kwh <= 500):
            preco = 0.4
            total = kwh * preco
            print(F'Tipo de instalação: {inst} | kWh gasto: {kwh} | Total a pagar: R$ {total:.2f}')
        elif(kwh > 500):
            preco = 0.65
            total = kwh * preco
            print(F'Tipo de instalação: {inst} | kWh gasto: {kwh} | Total a pagar: R$ {total:.2f}')
        else:
            print('Valor kWh inválido')
    elif(inst == 'I'):
        if(kwh > 0 and kwh <= 100):
            preco = 0.55
            total = kwh * preco
            print(F'Tipo de instalação: {inst} | kWh gasto: {kwh} | Total a pagar: R$ {total:.2f}')
        elif(kwh > 1000):
            preco = 0.60
            total = kwh * preco
            print(F'Tipo de instalação: {inst} | kWh gasto: {kwh} | Total a pagar: R$ {total:.2f}')
        else:
            print('Valor kWh inválido')
    else:
        if(kwh > 0 and kwh <= 5000):
            preco = 0.55
            total = kwh * preco
            print(F'Tipo de instalação: {inst} | kWh gasto: {kwh} | Total a pagar: R$ {total:.2f}')
        elif(kwh > 5000):
            preco = 0.60
            total = kwh * preco
            print(F'Tipo de instalação: {inst} | kWh gasto: {kwh} | Total a pagar: R$ {total:.2f}')
        else:
            print('Valor kWh inválido')
else:
    print('Tipo de instalação inválido, valor verificar.')