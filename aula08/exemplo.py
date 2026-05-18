def calcular_bonus(x):
    b = x * 0.1
    t = x + b   
    # print(b)
    # print(t)
    return b, t


n = float(input('\nInforme o valor da venda: '))

if n > 12000:
    # bônus
    bonus, total = calcular_bonus(n)
    print(f'\nValor da venda: R$ {n:.2f}')
    print(f'Valor do bônus: R$ {bonus:.2f}')
    print(f'Valor da venda: R$ {total:.2f}')
else:
    print(f'\nValor da venda: R$ {n:.2f}')
    print('Sem bônus')
