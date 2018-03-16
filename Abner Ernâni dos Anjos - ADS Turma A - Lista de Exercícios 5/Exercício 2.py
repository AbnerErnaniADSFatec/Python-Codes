i= 1
while 9 > i:
    if i != 3:
        j = 1
        while 6 > j:
            print('oi')
            j += 1
    i += 1
print((i-1)*j)
'''
1º while conta de 1 até 9;
2º while conta de 1 até 6;
porém o 2º while é executado 9 vezes de 1 até 6 menos uma em i é diferente de
3, (9-1)*6 = 9
'''
