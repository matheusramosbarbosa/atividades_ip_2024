# #Atividade 10 da Lista 1 

x, operador, y = int(input()), input(), int(input())

# if operador == "+":
#     z = x + y
#     print(f"{z}")
# elif operador == "-":
#     z = x - y
#     print(f"{z}")
# elif operador == "*":
#     z = x * y
#     print(f"{z}")
# elif operador == "/" and y != 0:
#     z = x // y
#     print(f"{z}")
# else:
#     print("Erro: operador não reconhecido.")

print(f"{x + y}") if operador == "+" else print(f"{x - y}") if operador == "-" else print(f"{x * y}") if operador == "*" else print(f"{x // y}") if operador == "/" and y != 0 else print("Erro: operador não reconhecido.")
