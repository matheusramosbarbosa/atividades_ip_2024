#Atividade 2 da Lista 1
#pistas: Mônaco, Ímola e Spa-Francorchamps
#ordem: Mônaco interior à Ímola, Ímola anterior à Spa-Francorchamps

#Inputs exigidos pelo desafio
velocidade_maxima = int(input())
tempo = input()

#Variáveis de apoio para ajudar na organização das condições, definindo o clima
sol = "ensolarado"
chuva = "chuvoso"
nevoa = "neblina"

#Condições para definir em qual pista Senna corria nesse dia
if velocidade_maxima >= 250 and velocidade_maxima <= 260 and (tempo == sol or tempo == chuva):
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
elif velocidade_maxima < 250 and tempo == nevoa:
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
elif velocidade_maxima >= 261 and velocidade_maxima <= 285 and (tempo == sol or tempo == chuva):
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
elif velocidade_maxima < 260 and tempo == nevoa:
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
elif velocidade_maxima >= 286 and velocidade_maxima <= 310 and (tempo == sol or tempo == chuva):
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")
elif velocidade_maxima < 285 and tempo == nevoa:
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")
