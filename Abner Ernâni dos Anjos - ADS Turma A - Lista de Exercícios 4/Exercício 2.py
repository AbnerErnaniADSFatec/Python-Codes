a=[]
impar=[]
par=[]
import random
for x in range(20):
    n= random.randint(1,100)
    a.append(n)
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
print('Inteiros Sorteados:',a)
par.sort()
print('Números pares:',par)
impar.sort()
print('Números impares:',impar)
