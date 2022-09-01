total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade? ')
    if idade == 'sair':
        break

    # Para não dar problema com o "sair":
    idade = int(idade)
    total += 1

    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print(f'Total de pessoas: {total}')
print(f'Total de arrecadado: R$ {dinheiro:.2f}')
print(f'Media arrecadada: R$ {media:.2f}')