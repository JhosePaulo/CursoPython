dias = int(input('Quantos dias foi alugado: '))
km = float(input('Quantos Km rodado: '))
valor1 = (dias * 60)
valor2 = (km * 0.15)

print('Voce tera que pagar pelo dias alugado: R$ {:.2f} e o valor pecorrido R$ {:.2f} o total fica R$ {:.2f}'.format(valor1, valor2, (valor1 + valor2)))
