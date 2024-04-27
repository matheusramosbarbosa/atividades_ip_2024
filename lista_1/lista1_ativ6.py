#Atividade 6 da Lista 1

#Inputs exigidos pelo desafio
construtor_1 = input()
posicao_1 = int(input())
salario_1 = int(input()) #Em milhões

construtor_2 = input()
posicao_2 = int(input())
salario_2 = int(input()) #Em milhões

#Variáveis de apoio
p_final = 0
p_final_2 = 0

#------------ Condições das Pontuações

#Construtor 1
if construtor_1 == "Red Bull":
    p_final += 3
elif construtor_1 == "McLaren":
    p_final += 2
elif construtor_1 == "Mercedes" or construtor_1 == "Aston Martin":
    p_final += 1

if posicao_1 == 1:
    p_final += 3
elif posicao_1 == 2:
    p_final += 2

if posicao_1 < 3:
    p_final += salario_1 // 4


#Construtor 2
if construtor_2 == "Red Bull":
    p_final_2 +=3
elif construtor_2 == "McLaren":
    p_final_2 += 2
elif construtor_2 == "Mercedes" or construtor_1 == "Aston Martin":
    p_final_2 += 1

if posicao_2 == 1:
    p_final_2 += 3
elif posicao_2 == 2:
    p_final_2 += 2

if posicao_2 < 3:
    p_final_2 += salario_2 // 4


#Condições de aceitação da proposta
if construtor_1 == "Red Bull":
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_1}, que pontuou {p_final}.')
elif construtor_2 == "Red Bull":
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_2}, que pontuou {p_final_2}.')
elif construtor_1 == "Red Bull" and construtor_2 == "Red Bull":
    if p_final > p_final_2:
        print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_1}, que pontuou {p_final}.')
    elif p_final < p_final_2:
        print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_2}, que pontuou {p_final_2}.')
    elif p_final == p_final_2:
        print(f'As duas são ótimas opções! Vamos, Sainz!!')
elif (posicao_1 == 3 and posicao_2 == 3) or (construtor_1 == "Ferrari" and construtor_2 == "Ferrari"):
    print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
elif posicao_1 == 3 and construtor_2 == "Ferrari":
    print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
elif posicao_2 == 3 and construtor_1 == "Ferrari":
    print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
elif (posicao_1 < 3 and posicao_2 == 3) and construtor_1 != "Ferrari":
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_1}, que pontuou {p_final}.')
elif (posicao_1 == 3 and posicao_2 < 3) and construtor_2 != "Ferrari":
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_2}, que pontuou {p_final_2}.')
elif (posicao_1 <= 2 and posicao_2 <= 2) and construtor_1 != "Ferrari" and construtor_2 != "Ferrari":
    if p_final > p_final_2:
        print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_1}, que pontuou {p_final}.')
    elif p_final < p_final_2:
        print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_2}, que pontuou {p_final_2}.')
    elif p_final == p_final_2:
        print(f'As duas são ótimas opções! Vamos, Sainz!!')
elif (posicao_1 <= 2 and posicao_2 <= 2) and construtor_2 == "Ferrari":
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_1}, que pontuou {p_final}.')
elif (posicao_1 <= 2 and posicao_2 <= 2) and construtor_1 == "Ferrari":
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor_2}, que pontuou {p_final_2}.')