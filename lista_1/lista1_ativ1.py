#Atividade 1 da Lista 1

#Inputs exigidos pelo desafio
piloto = input()
distancia = float(input())
tempo = float(input())

#Cálculo da velocidade média
v_media = distancia / tempo

#Condições para definir qual foi o comentário sobre o rendimento do piloto
if v_media > 227:
    print(f'{piloto} se deu muito bem na prova de hoje!!')
elif v_media == 227:
    print(f'{piloto} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!')
else:
    print(f'{piloto} não se deu tão bem. É preciso melhorar isso!')
