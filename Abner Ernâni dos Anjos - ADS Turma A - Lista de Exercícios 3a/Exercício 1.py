x= int(input('Digite um número entre 0 e 10: '))
while x < 0 or x > 10:
    print('Número Inválido, Menor que 0 ou maior que 10')
    x= int(input('Digite um número entre 0 e 10: '))
if 0 < x < 10:
    print('Número Válido. entre 0 e 10.')
