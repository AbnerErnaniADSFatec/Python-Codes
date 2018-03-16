s= float(input('Distância a percorrer (Km): '))
v= float(input('Velocidade média esperada (Km/h): '))
te= s/v
h= int(te)
m= (float(te) - int(te))*60
print('Com uma distância de %.1f' %s,'Km, e uma velocidade média esperada de %.1f Km/h' %v,'. É estimado um tempo de viagem de %.0f horas' %h,'e %.0f minutos' %m)
