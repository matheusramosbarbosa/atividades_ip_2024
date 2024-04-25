#Exercício 2

#Programa para ler três lados de um triângulo e dizer o tipo (equilátero, isósceles ou escaleno, ou não é triângulo)

lado_a = int(input('Ponha o valor do lado a: '))
lado_b = int(input('Ponha o valor do lado b: '))
lado_c = int(input('Ponha o valor do lado c: '))

if ((lado_a + lado_b) > lado_c) and ((lado_b + lado_c) > lado_a) and ((lado_a + lado_c) > lado_b):
    print('É um triângulo!')
    if (lado_a == lado_b) or (lado_b == lado_c):
        print('É um triângulo isósceles!')
    elif lado_a != lado_b != lado_c:
        print('É um triângulo escaleno!')
    elif lado_a == lado_b == lado_c:
        print('É um triângulo equilátero!')
else:
    print('Não é um triângulo! :(')