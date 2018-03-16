n1= int(input('1° Número: '))
n2= int(input('2° Número: '))
a= n1
b= n2
while n1 % n2:
    n1, n2 = n2, n1 % n2
print('O máximo divisor comum de %d e %d é %d.' %(a,b,n2))
