#nome = str(input('qual seu nome? '))
#print('Prazer em ter conhecer {}'.format(nome))

n1 = int(input('Primeiro valor: '))
n2 = int(input('segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A Soma e: {}, A multi e: {}, e a divisao e: {:.3f}'.format(s, m, d), end=' ')

print('Divisao inteira: {} e potencia {}'.format(di, e))


