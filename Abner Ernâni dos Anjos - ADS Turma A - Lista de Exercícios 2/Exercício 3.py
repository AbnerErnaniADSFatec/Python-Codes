peso = float(input('Digite o peso dos Peixes(Kg): '))
if peso > 50:
    print('Você exedeu o limite de peso.')
    pex = peso - 50
    multa = pex * 4
    print('Multa = R$ %.2f' %multa)
    print('Excesso = %.1fKg' %pex)
else:
    print('Você está dentro do limite de peso.')
    print('Multa = R$ 0.00')
