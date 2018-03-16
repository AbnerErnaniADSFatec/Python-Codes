a=[]
import random
for x in range(10):
    n= random.randint(1,100)
    a.append(n)
print('Inteiros Sorteados: ', a)
a.sort()
print('O maior número é',a[9],'e  o menor número é',a[0])
