def calculo_desconto(x):
    d = n * 0.16
    t = n - d
    return d, t


n = float(input('\nInforme o valor da compra: R$ '))

if n > 250:
    desconto, total = calculo_desconto(n)
    print(f'\nValor da compra: R$ {n:.2f}')
    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Valor final: R$ {total:.2f}')
else:
    print(f'\nValor da compra: R$ {n:.2f}')
    