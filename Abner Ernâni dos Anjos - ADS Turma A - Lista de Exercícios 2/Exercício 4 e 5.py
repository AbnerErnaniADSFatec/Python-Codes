a= int(input('Digite o 1º número: '))
b= int(input('Digite o 2º número: '))
c= int(input('Digite o 3º número: '))
if a > c and a > b:
    print('O maior número é o 1º número, %d.' %a)
if b > a and b > c:
    print('O maior número é o 2º número, %d.' %b)
if c > b and c > a:
    print('O maior número é o 3º número, %d.' %c)
if a < c and a < b:
    print('O menor número é o 1º número, %d.' %a)
if b < a and b < c:
    print('O menor número é o 2º número, %d.' %b)
if c < b and c < a:
    print('O menor número é o 3º número, %d.' %c)
elif a==b==c:
    print('Os números são iguais.')
elif a!=c and a==b:
    print('O 1º e 2º número são iguais')
elif b!=a and b==c:
    print('O 2º e 3º número são iguais')
elif c!=b and c==a:
    print('O 1º e 3º número são iguais')
if a!=b!=c:
    print('Os números são diferentes')
