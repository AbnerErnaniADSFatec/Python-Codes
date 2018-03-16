x= int(input('Insira um número inteiro: '))
div= [1]
d= 2
while x > 1:
    if x%d == 0:
        x = x/d
        div.append(d)
    else:
        d += 1
print(div)
