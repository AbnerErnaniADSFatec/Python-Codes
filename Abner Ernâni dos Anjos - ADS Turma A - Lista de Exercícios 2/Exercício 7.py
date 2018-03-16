mq= float(input('Medida da área a ser pintada em metros quadrados: '))
qml= (1/3) * mq
if qml <= 18:
    print('Será necessário 1 lata de tinta')
    print('No valor de R$ 80,00')
else:
    qlt= qml / 18
    t= (int(qlt) + 1) * 80
    total= int(qlt) + 1
    print('Serão precisos %d latas de tinta para pintar %.2f metros quadrados' %(total,mq))
    print('Total a pagar: R$ %.2f' %t)
