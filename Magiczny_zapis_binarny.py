wejście = int(input('Podaj liczbe:'))

tabela = []

while wejście>0:
    reszta = wejście % 2
    wejście = wejście // 2
    tabela.append(str(reszta))
zm = ''.join(tabela)
print(zm[::-1])