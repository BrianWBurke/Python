palavras = ('Maria', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print(F'\nPalavra {palavra.upper()}. Vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
