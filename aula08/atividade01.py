# O pescador João, que atua na região costeira de Santa Catarina, procurou sua empresa de tecnologia para resolver uma necessidade que ele enfrenta no dia a dia. 
# De acordo com o regulamento de pesca do estado, a quantidade máxima permitida de peixes por dia é de 100 quilos. 
# Quando esse limite é ultrapassado, o pescador deve pagar uma multa de R$ 4,00 por quilo excedente. 

# João precisa de um programa simples, que ele possa usar no celular para informar o peso total de peixes pescados no dia, e assim verificar se haverá multa ou não. Caso ultrapasse o limite, o sistema deve calcular o valor da multa automaticamente. 

# Requisito: 
# Crie um algoritmo que: 

# Receba o peso total de peixes pescados no dia 

# Verifique se houve excesso 

# Calcule e retorne o valor da multa, se houver 

# Mostre a mensagem correspondente na tela

def calculo_multa(x):
    e = x - 100
    m = e * MULTA
    return e, m

LIMITE = 100
MULTA = 4.00
qtd_pesc = float(input('\nInforme o peso pescado (Kg): '))

if qtd_pesc > LIMITE:
    excedente, mul = calculo_multa(qtd_pesc)
    print(f'\nTotal pescado (Kg): {qtd_pesc:.2f}')
    print(f'Excedente pescado (Kg): {excedente:.2f}')
    print(f'Total da multa: R$ {mul:.2f}')
else:
    print(f'\nTotal pescado (Kg): {qtd_pesc}')
    print('Sem multa')