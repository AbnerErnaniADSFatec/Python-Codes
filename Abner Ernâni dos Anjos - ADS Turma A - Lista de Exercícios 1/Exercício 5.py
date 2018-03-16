pm= float(input('Digite o preço da mercadoria ($): '))
p= float(input('Digite a porcentagem de desconto (%): '))
ppm= pm*(p/100)
total= pm-ppm
print('A mecadoria sofreu um desconto de $ %.2f' %ppm, 'do valor,o total a pagar é $ %.2f' %total)
