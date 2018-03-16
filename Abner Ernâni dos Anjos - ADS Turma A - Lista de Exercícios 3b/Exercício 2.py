print('CÁLCULO DO TROCO')
a= float(input('Valor da Conta (R$): '))
b= float(input('Valor pago (R$): '))
t= b - a
qdn50,qdn20,qdn10,qdn5,qdn2,qdn1=0,0,0,0,0,0
print('O caixa terá que te dar de troco:')
if t >= 50:
    while t >= 50:
        t= t - 50
        qdn50 += 1
    if t < 50:
        print(qdn50,'notas de 50')
if t >= 20:
    while t >= 20:
        t= t - 20
        qdn20 += 1
    if t < 20:
        print(qdn20,'notas de 20')
if t >= 10:
    while t >= 10:
        t= t - 10
        qdn10 += 1
    if t < 10:
        print(qdn10,'notas de 10')
if t >= 5:
    while t >= 5:
        t= t - 5
        qdn5 += 1
    if t < 5:
        print(qdn5,'notas de 5')
if t >= 2:
    while t >= 2:
        t= t - 2
        qdn2 += 1
    if t < 2:
        print(qdn2,'notas de 2')
if t >= 1:
    while t >= 1:
        t= t - 1
        qdn1 += 1
    if t < 1:
        print(qdn1,'notas de 1')

