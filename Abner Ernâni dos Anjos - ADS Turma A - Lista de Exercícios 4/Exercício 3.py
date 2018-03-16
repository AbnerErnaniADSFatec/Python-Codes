i= 0
a=[]
b=[]
c=[]
import random
for x in range(10):
    n= random.randint(1,100)
    a.append(n)
for x in range(10):
    n= random.randint(1,100)
    b.append(n)
while i < 10:
    c.append(a[i])
    c.append(b[i])
    i += 1
print('1ª vetor:', a)
print('2ª vetor:', b)
print('3ª vetor:', c)
