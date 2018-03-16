print('A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra deformação é simples:')
print('os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.')
a,b= 0,1
n= int(input('Digite um número inteiro: '))
c= 2
while c <= n:
    a,b = b,b + a
    c += 1
print('Seu número correspondente na sequência fibonacci é %d' %b)
