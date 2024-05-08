#Atividade 9 da Lista 1

#---Variáveis com textos para evitar erros na sintaxe das condições
#climas
chuva = "chuva"
sol = "sol"

#dificuldade
baixa = "baixa"
media = "média"
alta = "alta"

#tipos de pneus
duro = "duro"
medio = "médio"
macio = "macio"

#Variável de apoio
durabilidade = 0

#Inputs exigidos pelo desafio
voltas = int(input())
clima = input()
dificuldade = input()
tipo_pneu = input()

#Condições para atribuição de valor de durabilidade a com base no tipo de pneu
if tipo_pneu == chuva:
    durabilidade = 50
elif tipo_pneu == macio:
    durabilidade = 50
elif tipo_pneu == medio:
    durabilidade = 70
elif tipo_pneu == duro:
    durabilidade = 90

#Condição para pneus que não são propícios para o tipo de clima
if tipo_pneu == chuva and clima == sol:
    voltas *= 15
    durabilidade = durabilidade - voltas
elif tipo_pneu != chuva and clima == chuva:
    voltas *= 15
    durabilidade = durabilidade - voltas

#Condições de atribuição de valor à durabilidade com base em diversos fatores
if clima == sol and (dificuldade == baixa or dificuldade == media) and (tipo_pneu == macio or tipo_pneu == medio):
    voltas *= 2
    durabilidade = durabilidade - voltas
elif clima == sol and dificuldade == alta and tipo_pneu == macio:
    voltas *= 3
    durabilidade = durabilidade - voltas
elif clima == sol and dificuldade == alta and tipo_pneu == duro:
    durabilidade = durabilidade - voltas
elif clima == chuva and dificuldade == baixa and tipo_pneu == chuva:
    durabilidade = durabilidade - voltas
elif clima == chuva and dificuldade == media and tipo_pneu == chuva:
    voltas *= 2
    durabilidade = durabilidade - voltas
elif clima == chuva and dificuldade == alta and tipo_pneu == chuva:
    voltas *= 3
    durabilidade = durabilidade - voltas

#Condições com os outputs finais
if durabilidade >= 20:
    print(f"A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durabilidade}.")
elif durabilidade < 20:
    print(f"Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durabilidade} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.")
