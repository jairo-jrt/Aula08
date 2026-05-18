# A equipe de saúde da academia Vida Ativa, localizada em São Francisco / Niterói, está modernizando o sistema de atendimento.
# A equipe da Vida Ativa solicitou a adição de uma nova funcionalidade, a fim de agilizar as avaliações físicas dos alunos. 
# A gerente Camila informou a necessidade de um programa, onde eles possam inserir os dados de altura e peso de uma ou mais pessoas, 
# e fosse possível o programa calcular o IMC (Índice de Massa Corporal).
# Além disso, ela gostaria que também fosse informado a classificação correspondente de cada pessoa, com base no resultado do cálculo do IMC. 

# A fórmula utilizada para o cálculo é: 
# IMC = peso / (altura × altura)

def calculo_imc(x, y):
    i = x / (y ** 2)
    return i


while True:
    print('\nCálculo IMC')
    
    peso = float(input('\nInforme o peso (Kg): '))
    altura = float(input('Informe a altura (m): '))

    imc = calculo_imc(peso, altura)
    
    print(f'\nIMC = {imc:.2f}')

    match imc:

        case imc if imc < 16.9:
            print('Muito abaixo do peso')
        case imc if imc <= 18.4:
            print('Abaixo do peso')
        case imc if imc <= 24.9:
            print('Peso normal')
        case imc if imc <= 29.9:
            print('Acima do peso')
        case imc if imc <= 34.9:
            print('Obesidade Grau I')
        case imc if imc <= 40:
            print('Obesidade Grau II')
        case imc if imc > 40:
            print('Obesidade Grau III')
    
    continuar = input('\nDeseja continuar? [S/N]: ').upper().strip()[0]
    if continuar != 'S':
        break


