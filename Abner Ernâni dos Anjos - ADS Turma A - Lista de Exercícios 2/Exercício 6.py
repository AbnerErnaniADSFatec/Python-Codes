qgh= float(input('Quanto você ganha por hora(R$): '))
nht= float(input('Número de horas trabalhadas no mês: '))
sht= qgh * nht
ir= sht * (11/100)
inss= sht * (8/100)
sind= sht * (5/100)
total= ir + inss + sind
sl= sht - total
print ('+Salário Bruto:\t\t R$ %10.2f' %sht)
print ('-IR:\t\t\t R$ %10.2f' %ir)
print ('-INSS:\t\t\t R$ %10.2f' %inss)
print ('-Sindicato:\t\t R$ %10.2f' %sind)
print ('=Salário Líquido:\t R$ %10.2f' %sl)
