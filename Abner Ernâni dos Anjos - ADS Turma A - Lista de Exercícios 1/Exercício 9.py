kmr= float(input('Digite a quantidade de quilometros rodados (Km): '))
dp= int(input('Digite a quantidade de dias em que passou com o carro: '))
pap= (dp * 60) + (kmr * 0.15)
print('Pela tabela de preços, onde são $60.00/dia e $0.15/quilometros rodados, calcula-se um total a pagar de $%.2f' %pap)
