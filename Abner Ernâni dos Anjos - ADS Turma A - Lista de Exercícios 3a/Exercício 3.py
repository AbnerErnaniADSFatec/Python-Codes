print('O país A tem uma população de 80000 habitantes com uma taxa anual de crescimento de 3%.')
print('O país B tem uma população de 200000 habitantes com uma taxa anual de crescimento de 1.5%.')
a= 80000
b= 200000
anos= 0
while a < b:
    a= (a * (3/100)) + a
    b= (b * (1.5/100)) + b
    anos += 1
if a > b:
    print('A população do país A irá ultrapassar a do país B em %d anos.' %anos)
    print('População de A= %d' %a)
    print('População de B= %d' %b)
