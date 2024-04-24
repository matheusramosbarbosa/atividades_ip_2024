#Ordem alfabética: Lewis, Max e Valtteri

p_lewis = int(input())
c_lewis = int(input())
p_max = int(input())
c_max = int(input())
p_valtteri = int(input())
c_valtteri = int(input())

if c_lewis <= 10:
    p_lewis = p_lewis + 5
if c_max <= 10:
    p_max = p_max + 5
if c_valtteri <= 10:
    p_valtteri = p_valtteri + 5


vencedor = ""
p_vencedor = 0

if (p_lewis == p_max) and (p_lewis > p_valtteri):
    # print(f"Lewis Hamilton ganhou a competição com {p_lewis} pontos!")
    vencedor = "Lewis Hamilton"
    p_vencedor = p_lewis
elif (p_max == p_valtteri) and (p_max > p_lewis):
    vencedor = "Max Verstappen"
    p_vencedor = p_max
    # print(f"Max Verstappen ganhou a competição com {p_max} pontos!")
elif (p_max > p_valtteri) and (p_max > p_lewis):
    vencedor = "Max Verstappen"
    p_vencedor = p_max
    # print(f"Max Verstappen ganhou a compteição com {p_max} pontos!")
elif (p_valtteri > p_max) and (p_valtteri > p_lewis):
    vencedor = "Valtteri Bottas"
    p_vencedor = p_valtteri
    # print(f"Valtteri Bottas ganhou a competição com {p_valtteri} pontos!")
elif (p_lewis > p_max) and (p_lewis > p_valtteri):
    vencedor = "Lewis Hamilton"
    p_vencedor = p_lewis
    # print(f"Lewis Hamilton ganhou a compteição com {p_lewis} pontos!")
elif p_lewis == p_valtteri == p_max:
    vencedor = "Lewis Hamilton"
    p_vencedor = p_lewis
    # print(f"Lewis Hamilton ganhou a competição com {p_lewis} pontos!")

print(f"{vencedor} ganhou a competição com {p_vencedor} pontos!")
