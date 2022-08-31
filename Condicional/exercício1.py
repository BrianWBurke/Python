# Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando
# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em cada matéria e informa, na tela, se ele passou de ano ou não.

x = float(input('Insira a primeira nota: '))
y = float(input('Insira a segunda nota: '))
z = float(input('Insira a terceira nota: '))

notaF = (x + y + z) / 3

print(f'Nota 1: {x:.2} | Nota 2: {y:.2} | Nota 3: {z:.2} | Nota Final: {notaF:.2}')

if (notaF >= 7):
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')