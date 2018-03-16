d= int(input('Quantidade de dias: '))
h= int(input('Quantidade de horas: '))
m= int(input('Quantidade de minutos: '))
s= int(input('Quantidade de segundos: '))
ds= (d*24*60*60)
hs= (h*60*60)
ms= (m*60)
total= ds+hs+ms+s
print(d,'dias,',h,'horas,',m,'minutos e',s,'segundos se calcula um total de',total,'segundos')
