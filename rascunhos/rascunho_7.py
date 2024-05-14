numero_inteiro = int(input("Digite um número inteiro maior que 0 e menor que 100: "))
variavel_apoio = ""
while ((numero_inteiro < 0) or (numero_inteiro > 100)):
    print("Desculpe, esse número é menor que 0 ou maior que 100!")
    numero_inteiro = int(input("Digite um número inteiro maior que 0 e menor que 100: "))

while ((numero_inteiro > 0) and (numero_inteiro < 99)):
    if numero_inteiro % 2 == 0:
        numero_inteiro += 1
        variavel_apoio += f"{numero_inteiro}, "
    elif (numero_inteiro % 2 == 1) and (numero_inteiro <= 95):
        variavel_apoio += f"{numero_inteiro}, "
        numero_inteiro += 2
    elif (numero_inteiro == 97):
        numero_inteiro += 2
        variavel_apoio += f"{numero_inteiro}."
        numero_inteiro += 2
else:
    print(variavel_apoio)
