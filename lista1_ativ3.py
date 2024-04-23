#Atividade 3 da Lista 1
#colocação de 1 a 10, mas as condições não exigem a lista
#é o bra do bra

pontuacaoCharles = int(input())
pontuacaoMax = int(input())

if pontuacaoCharles == 0:
    print("Oxe! E vai morrer por causa de 25 pontos?")
elif pontuacaoCharles == 25:
    print("O meu favorito venceu! Pode torar o aco Verstappen")
elif pontuacaoCharles == 18 or pontuacaoCharles == 15:
    print("Esse Charles eh arretado mesmo")
elif pontuacaoCharles == 12 or pontuacaoCharles == 10:
    print("Ele eh desenrolado demais")

if pontuacaoCharles >= (pontuacaoMax - 4) and pontuacaoCharles < pontuacaoMax:
     print("Ta com a molestia, vai perder para Max Verstappen eh")
elif pontuacaoCharles <= (pontuacaoMax + 4) and pontuacaoCharles > pontuacaoMax:
    print("Ta com a molestia, vai perder para Max Verstappen eh")
elif pontuacaoCharles > (pontuacaoMax + 4):
    print("Deu o sangue")
