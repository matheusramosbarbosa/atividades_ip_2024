#Atividade 5 da lista 1

direcao = ""
direcao2 = ""
retorno_01 = ""
retorno_02 = ""
retorno_direcao = ""
retorno_direcao2 = ""
curva = "Tem uma curva vindo aí, me ajuda!"

#Variáveis com input e condição se a mensagem for pedindo direção
frase_01 = input()
if frase_01 == curva:
    direcao = input()

frase_02 = input()
if frase_02 == curva:
    direcao2 = input()

#Condição para caso o usuário ponha mensagem de curva

#Variáveis que armazenam as frases (para simplificar mais as condicionais)
pisa = "PISA FUNDO"
ultrapassa = "Ultrapassa ele agora!"
freia = "FREIA AGORA E ME DIZ PARA QUE LADO É"
entao = "ENTÃO VIRA LOGO!"
virar = "É SÓ VIRAR!"
ajuda = "Assim não tem como te ajudar, amiga"
amiga = "Amiga, calma! Tem um pit stop na tua frente…"
eita = "Eita, não entendi nada…"
lets = "LET'S RIDE!"


#Condições para a primeira frase
if frase_01 == "TÔ EM ÚLTIMO!":
    retorno_01 = pisa
elif frase_01 == "Esse cara não sai da minha frente...":
    retorno_01 = ultrapassa
elif frase_01 == curva:
    retorno_01 = freia
    if direcao == "DIREITA":
        retorno_direcao = entao
    elif direcao == "ESQUERDA":
        retorno_direcao = virar
    else:
        retorno_direcao = ajuda
elif frase_01 == "MEU PNEU FUROU SOCORRO!":
    retorno_01 = amiga
else:
    retorno_01 = eita

#Condições para a segunda frase
if frase_02 == "TÔ EM ÚLTIMO!":
    retorno_02 = pisa
elif frase_02 == "Esse cara não sai da minha frente...":
    retorno_02 = ultrapassa
elif frase_02 == curva:
    retorno_02 = freia
    if direcao2 == "DIREITA":
        retorno_direcao2 = entao
    elif direcao2 == "ESQUERDA":
        retorno_direcao2 = virar
    else:
        retorno_direcao2 = ajuda
elif frase_02 == "MEU PNEU FUROU SOCORRO!":
    retorno_02 = amiga
else:
    retorno_02 = eita

#Condições para os outputs finais
if frase_01 == curva:
    print(f"{retorno_01}")
    print(f"{retorno_direcao}")
else:
    print(f"{retorno_01}")

if frase_02 == curva:
    print(f"{retorno_02}")
    print(f"{retorno_direcao2}")
else:
    print(f"{retorno_02}")

print(f"{lets}")