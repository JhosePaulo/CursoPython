larg = float(input('Largura da parede: '))
alt = float(input('Altura da Parede: '))
area = larg * alt

print('Sua parede tem a dimensao de {} x {} e sua area e de {}m2.'.format(larg, alt, area))

tinta = area / 2

print('A quantidade de tinta necessaria sera: {}L.'.format(tinta))
