# #Atividade 10 da Lista 1 

x, operador, y, soma, subtracao, multiplicacao, divisao = int(input()), input(), int(input()), 0, 0, 0, 0
# soma = x + y if operador == "+" else subtracao = x - y if operador == "-"


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

#--------------------------------------------------------------
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")
# do site indicado ^^^^^^^^^^^^^^^^^^