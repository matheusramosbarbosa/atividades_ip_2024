#Atividade 10 da Lista 1 

x = int(input())
operador = input()
y = int(input())
z = 0

if operador == "+":
    z = x + y
    print(f"{z}")
elif operador == "-":
    z = x - y
    print(f"{z}")
elif operador == "*":
    z = x * y
    print(f"{z}")
elif operador == "/" and y != 0:
    z = x // y
    print(f"{z}")
else:
    print("Erro: operador não reconhecido.")