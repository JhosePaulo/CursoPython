cart = float(input('Quanto vc tem na carteira ? R$'))
dolar = cart / 5.06

print('Com esses R${:.2f}, Voce pode comprar {:.2f} em dolar'.format(cart, dolar))
