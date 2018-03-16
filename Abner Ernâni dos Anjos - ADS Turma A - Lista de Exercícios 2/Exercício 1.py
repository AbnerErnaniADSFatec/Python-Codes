a= int(input('Valor de A: '))
b= int(input('Valor de B: '))
c= int(input('Valor de C: '))
if a + b > c and a + c > b and b + c > a:
    print('Essas medidas formam um triângulo')
    if a==b==c:
        print('É um triângulo Equilátero')
    if a==b and a!=c and b!=c:
        print('É um triângulo Isóceles')
    if a==c and a!=b and b!=c:
        print('É um triângulo Isóceles')
    if a==b and a!=b and a!=c:
        print('É um triângulo Isóceles')
    if a!=b and a!=c and b!=c:
        print('É um triângulo Escaleno')
else:
    print('Essas medidas não podem formar um triângulo')
    print('Um dos lados é maior que a soma dos outros')
