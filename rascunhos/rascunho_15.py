# escreva um programa para:
# Ler um inteiro do teclado
# - use um do-while para garantir que o programa só continua se for digitado um número maior que 0
# Calcular o fatorial desse número (usando for)
# fatorial x = (1, se x = 0) ou (x * (x-1) * (x-2) * ... * 1, se x > 0)
# imprimir o resultado!
# i++ ou i-- é o mesmo de i = i + 1 e i = i - 1

numero = int(input("Digite o número: "))
resultado = 0
i = numero

while numero <= 0:
    numero = int(input("Digite o número: "))

for i in range (1, numero, 1):
    resultado *= (numero - i)
else:
    print(resultado)