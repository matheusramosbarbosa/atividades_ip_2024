#Atividade 8 da Lista 1

#Variáveis com textos para evitar erros na sintaxe das condições
chuva = "chuvoso"
sol = "ensolarado"
nublado = "nublado"
alta = "alta"
moderada = "moderada"
baixa = "baixa"
bom = "bom"
ruim = "ruim"

#Inputs exigidos pelo desafio
condicoes_meteorologicas = input()
if condicoes_meteorologicas == chuva:
    pista_molhada = input()
    if pista_molhada == "True":
        pista_molhada = True
    elif pista_molhada == "False":
        pista_molhada = False

temperatura_pista = input()
desempenho_treinos = input()
posicao_largada = int(input())

print("Estratégia de prova de Max Verstappen!")

#Condições de clima e temperatura + respectivo print
if condicoes_meteorologicas == sol and temperatura_pista == alta:
    print("Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!")
elif condicoes_meteorologicas == sol and temperatura_pista != alta:
    print("Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.")
elif condicoes_meteorologicas == nublado and temperatura_pista == alta:
    print("Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!")
elif condicoes_meteorologicas == nublado and (temperatura_pista == baixa or temperatura_pista == moderada):
    print("Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!")
elif condicoes_meteorologicas == chuva and pista_molhada == True:
    print("Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.")
elif condicoes_meteorologicas == chuva and pista_molhada == False:
    print("Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!")

#Condições de largada
if posicao_largada == 1 and desempenho_treinos == bom:
    print("Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.")
elif posicao_largada == 1 and desempenho_treinos == ruim:
    print("Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.")
elif posicao_largada >= 2 and posicao_largada <= 12:
    print("Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.")
elif posicao_largada > 12:
    print("Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.")