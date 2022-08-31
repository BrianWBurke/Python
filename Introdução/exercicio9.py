# atribuir s1 = 'ant', s2 = 'bat' e s3 = 'cod'
# agora utilizando operadores + e *, crie as saídas a seguir: 'ant bat cod', 'ant ant ant ant ant ant ant ant ant ant', 'ant bat bat cod cod cod', 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat', 'batbatcod batbatcod batbatcod batbatcod batbatcod' 

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1 , s2 , s3)
print(10 * (s1 + ' '))
print(s1, 2 * (s2 + ' ') + 3 * (s3 + ' '))
print(7 * (s1 + ' ' + s2 + ' '))
print(5 * (2 * s2 + s3 + ' '))