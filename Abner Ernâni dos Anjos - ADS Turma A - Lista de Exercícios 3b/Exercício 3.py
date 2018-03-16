x= int(input('Insira um número inteiro: '))
a= 1
div= 0
while a <= x:
	if (x%a) == 0:
		div += 1
	a += 1
if div == 2:
	print ('%d é um número primo.' %x)
else:
	print ('%d não é um número primo.' %x)
