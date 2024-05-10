# Implemente um programa em Python para realizar uma operação de multiplicação através de múltiplas operações de soma.

numero_um = int(input("Digite aqui o primeiro número: "))
numero_dois = int(input("Agora digite quantas vezes ele vai ser multiplicado: "))
resultado = 0

while (numero_dois > 0):
    numero_dois -= 1
    resultado += numero_um
else:
    print(resultado)
