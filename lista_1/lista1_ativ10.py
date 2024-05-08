# #Atividade 10 da Lista 1 | Abaixo encontram-se os inputs exigidos pelo desafio e, abaixo dessa linha, as condições para chegar ao resultado da operação exigida pelo usuário.
x, operador, y = int(input()), input(), int(input())
print(f"{x + y}") if operador == "+" else print(f"{x - y}") if operador == "-" else print(f"{x * y}") if operador == "*" else print(f"{x // y}") if operador == "/" and y != 0 else print("Erro: operador não reconhecido.")


#O desafio define um limite de 3 linhas!