#Exercício 3
#Escreva um programa para ler dois valroes reais, correspondentes ao peso a à altura de uma pessoa, e calcular o Índice de Massa Corporal (IMC), pela fórmula: IMC = peso/atura**2. Em seguida, dar mensagem conforme a seguinte tabela:
peso = float(input('Ponha seu peso: '))
altura = float(input('Ponha sua altura: '))

calculo = (peso / altura**2)

if calculo <= 18.5:
    print('abaixo do peso')
elif calculo <= 25:
    print('peso normal')
elif calculo <= 30:
    print('acima do peso')
elif calculo > 30:
    print('obeso')