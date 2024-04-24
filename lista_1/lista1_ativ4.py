#Atividade 4 da lista 1

#Aqui encontram-se os inputs pedidos pelo desafio, onde p_{piloto} é a pontuação do piloto, e c_{piloto} é a colocação do piloto.
p_lewis = int(input())
c_lewis = int(input())
p_max = int(input())
c_max = int(input())
p_valtteri = int(input())
c_valtteri = int(input())

#Condição para definir as pontuações de acordo com a colocação do piloto, adicionando 5 pontos se no top 10.
if c_lewis <= 10:
    p_lewis = p_lewis + 5
if c_max <= 10:
    p_max = p_max + 5
if c_valtteri <= 10:
    p_valtteri = p_valtteri + 5

#Variáveis de ajuda, para definir o vencedor final (seu nome) e a pontuação do vencedor final.
vencedor = ""
p_vencedor = 0

#Condição para definição de vencedor e atribuição da pontuação do vencedor à variável de ajuda.
if (p_lewis == p_max) and (p_lewis > p_valtteri):
    vencedor = "Lewis Hamilton"
    p_vencedor = p_lewis
elif (p_max == p_valtteri) and (p_max > p_lewis):
    vencedor = "Max Verstappen"
    p_vencedor = p_max
elif (p_max > p_valtteri) and (p_max > p_lewis):
    vencedor = "Max Verstappen"
    p_vencedor = p_max
elif (p_valtteri > p_max) and (p_valtteri > p_lewis):
    vencedor = "Valtteri Bottas"
    p_vencedor = p_valtteri
elif (p_lewis > p_max) and (p_lewis > p_valtteri):
    vencedor = "Lewis Hamilton"
    p_vencedor = p_lewis
elif p_lewis == p_valtteri == p_max:
    vencedor = "Lewis Hamilton"
    p_vencedor = p_lewis

#Output final, print utilizando as variáveis de apoio.
print(f"{vencedor} ganhou a competição com {p_vencedor} pontos!")
