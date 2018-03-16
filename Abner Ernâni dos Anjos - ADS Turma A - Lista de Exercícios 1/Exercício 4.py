s= float(input('Digite o valor do salário($): '))
p= float(input('Digite a porcentagem de aumento(%): '))
ps= s * (p/100)
total= s + ps
print('Seu salário aumentou $',ps,' e seu valor final é $ %.2f' %total)
