numero = int(input("Digite um número maior que zero e menor que 100: "))
while ((numero < 0) or (numero > 100)):
  numero = int(input("Digite um número maior que zero e menor que 100: "))

if numero % 2 == 0:
  numero += 1
for numero in range (numero, 100, 2):
    print(f'{numero},', end=' ')
else:
    print(f'{numero}.')
