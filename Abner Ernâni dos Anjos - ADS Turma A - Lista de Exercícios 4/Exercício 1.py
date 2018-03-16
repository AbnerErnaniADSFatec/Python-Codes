a =[]
b = 0
c = 100
import random
for x in range(10):
    n = random.randint(1,100)
    a.append(n)
    if n > b:
        b = n
    if n < c:
        c = n
print('Inteiros Sorteados: ', a)
print('O maior número é',b,'e  o menor número é',c)
