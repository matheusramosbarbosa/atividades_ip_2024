#Atividade 3 da Lista 1

#Inputs exigidos pelo desafio, com a pontuação de Charles e a pontuação de Max
pontuacaoCharles = int(input())
pontuacaoMax = int(input())

#Condição para definir qual a mensagem que vai para o output, de acordo com a pontuação do Charles
if pontuacaoCharles == 0:
    print("Oxe! E vai morrer por causa de 25 pontos?")
elif pontuacaoCharles == 25:
    print("O meu favorito venceu! Pode torar o aco Verstappen")
elif pontuacaoCharles == 18 or pontuacaoCharles == 15:
    print("Esse Charles eh arretado mesmo")
elif pontuacaoCharles == 12 or pontuacaoCharles == 10:
    print("Ele eh desenrolado demais")

#Condição para definir se Charles possui uma diferença de 4 pontos do Max, para mais ou para menos
#Print caso Charles possua a diferença nessa faixa, ou, caso possua uma diferença bem maior em comparação a Max
if pontuacaoCharles >= (pontuacaoMax - 4) and pontuacaoCharles < pontuacaoMax:
     print("Ta com a molestia, vai perder para Max Verstappen eh")
elif pontuacaoCharles <= (pontuacaoMax + 4) and pontuacaoCharles > pontuacaoMax:
    print("Ta com a molestia, vai perder para Max Verstappen eh")
elif pontuacaoCharles > (pontuacaoMax + 4):
    print("Deu o sangue")
