valor = int(input('Digite o valor arredondado em reais: '))

while True:
    if valor >= 100:
        celulas100 = valor // 100
        valor -= celulas100 * 100
        print(f'Celulas de 100: {celulas100}')
        if not valor:
            break
    if valor >= 50:
        celulas50 = valor // 50
        valor -= celulas50 * 50
        print(f'Celulas de 50: {celulas50}')
        if not valor:
            break
    if valor >= 20:
        celulas20 = valor // 20
        valor -= celulas20 * 20
        print(f'Celulas de 20: {celulas20}')
        if not valor:
            break
    if valor >= 10:
        celulas10 = valor // 10
        valor -= celulas10 * 10
        print(f'Celulas de 10: {celulas10}')
        if not valor:
            break
    if valor >= 5:
        celulas5 = valor // 5
        valor -= celulas5 * 5
        print(f'Celulas de 5: {celulas5}')
        if not valor:
            break
    if valor:
        celulas1 = valor
        print(f'Celulas de 1: {celulas1}')
        break
