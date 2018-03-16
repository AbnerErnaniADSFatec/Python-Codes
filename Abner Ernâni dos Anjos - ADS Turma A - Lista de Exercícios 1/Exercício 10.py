qc= int(input('Quantidade de cigarros fumados por dia: '))
qaf= int(input('Há quantos anos você fuma: '))
tdc= (qc * 10 * qaf * 365)/(24*60)
total= (float(tdc) - int(tdc)) * 24
print('Você já perdeu %d dias' %tdc,'e %d horas de sua vida' %total)
