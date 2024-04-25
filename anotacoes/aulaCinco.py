#Exercício 1

#Escreva um programa para ler dois valores reais, x e y, correspondentes ás coordenadas de um ponto no plano e dizer em que quadrante se encontra, ou se está no eixo-x ou no eixo-y ou se está na origem.

x = float(input('Ponha o valor de x: '))
y = float(input('Ponha o valor de y: '))

if (x and y) == 0:
    print('Você está na origem.')
elif x == 0:
    print('Você está no eixo y!')
elif y == 0:
    print('Você está no eixo x!')
elif y > 0 and x > 0:
    print('Você está no 1º quadrante!')
elif y > 0 and x < 0:
    print('Você está no 2º qudrante!')
elif y < 0 and x < 0:
    print('Você está no 3º quadrante!')
elif y < 0 and x > 0:
    print('Você está no 4º quadrante!') 

    