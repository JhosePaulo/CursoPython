func =float(input('Qual o salario do funcionario: R$ '))
realj = func + (func * 15 / 100)

print('O Salario atual do func. R$ {:.2f}, com o reajuste de 15%, sera de R$ {:.2f}.'.format(func, realj))
