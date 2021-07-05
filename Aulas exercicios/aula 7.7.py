produto = float(input('Qual valor do produto, R$ '))
novo = produto - (produto * 5 / 100)
print('O produto que custa R$ {:.2f}, na promocao de 5% vai custar R$ {:.2f}'.format(produto, novo))

