#Atividade 7 da Lista 1

#Inputs exigidos pelo desafio
piloto_a = input()
tempo_a = float(input())
piloto_b = input()
tempo_b = float(input())
piloto_c = input()
tempo_c = float(input())

#Variáveis de apoio
primeiro = ""
tempo_primeiro = 0
segundo = ""
tempo_segundo = 0
terceiro = ""
tempo_terceiro = 0

#Condições para definição do pódio
if tempo_a < tempo_b < tempo_c:
    primeiro = piloto_a
    tempo_primeiro = tempo_a
    segundo = piloto_b
    tempo_segundo = tempo_b
    terceiro = piloto_c
    tempo_terceiro = tempo_c
elif tempo_a < tempo_c < tempo_b:
    primeiro = piloto_a
    tempo_primeiro = tempo_a
    segundo = piloto_c
    tempo_segundo = tempo_c
    terceiro = piloto_b
    tempo_terceiro = tempo_b
elif tempo_b < tempo_a < tempo_c:
    primeiro = piloto_b
    tempo_primeiro = tempo_b
    segundo = piloto_a
    tempo_segundo = tempo_a
    terceiro = piloto_c
    tempo_terceiro = tempo_c
elif tempo_b < tempo_c < tempo_a:
    primeiro = piloto_b
    tempo_primeiro = tempo_b
    segundo = piloto_c
    tempo_segundo = tempo_c
    terceiro = piloto_a
    tempo_terceiro = tempo_a
elif tempo_c < tempo_a < tempo_b:
    primeiro = piloto_c
    tempo_primeiro = tempo_c
    segundo = piloto_a
    tempo_segundo = tempo_a
    terceiro = piloto_b
    tempo_terceiro = tempo_b
elif tempo_c < tempo_b < tempo_a:
    primeiro = piloto_c
    tempo_primeiro = tempo_c
    segundo = piloto_b
    tempo_segundo = tempo_b
    terceiro = piloto_a
    tempo_terceiro = tempo_a

#Output final com mensagem do Galvão
print("E o Pódio do GP de Mônaco é:")
print(f"{primeiro} está no lugar mais alto do pódio com tempo de {tempo_primeiro} horas de corrida.")
print(f"{segundo} está no segundo lugar do pódio com tempo de {tempo_segundo} horas de corrida.")
print(f"{terceiro} está no terceiro lugar do pódio com tempo de {tempo_terceiro} horas de corrida.")
print(f"Galvão, temos um momento histórico da Fórmula 1, {primeiro} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_primeiro} horas de prova.")