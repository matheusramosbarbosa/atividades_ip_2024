# Atividade 8 da Lista 2

candidato_1 = input()
candidato_2 = input()
votos_populares1 = 0
votos_populares2 = 0
total_votos_candidato1 = 0
total_votos_candidato2 = 0
urna = True
taylor_roubou = "Taylor Swift roubou as urnas!"

while urna:
    if candidato_1 != "Kanye West" and candidato_2 != "Kanye West":
        print("Sem o Ye, sem eleição!")
        urna = False
    else:
        conjunto = input()
        if conjunto == "FIM":
            urna = False
        elif conjunto != "FIM" and urna: 
            x = conjunto.split(", ")
            estado, delegados = x
            delegados = int(delegados)
            votos_candidato1 = input()
            if votos_candidato1 != taylor_roubou:
                votos_candidato2 = input()
            while votos_candidato1 == taylor_roubou or votos_candidato2 == taylor_roubou:
                print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                votos_candidato1 = input()
                if votos_candidato1 != taylor_roubou:
                    votos_candidato2 = input()
            votos_candidato1 = int(votos_candidato1)
            votos_candidato2 = int(votos_candidato2)
            total_estado = votos_candidato1 + votos_candidato2
            if votos_candidato1 > votos_candidato2:
                y = (votos_candidato1 / total_estado) * 100
                y = int(y)
                print(f"{candidato_1} obteve maioria no(a) {estado} com {y}% dos votos.")
                total_votos_candidato1 += delegados
                votos_populares1 += votos_candidato1
            else:
                y = (votos_candidato2 / total_estado) * 100
                y = int(y)
                print(f"{candidato_2} obteve maioria no(a) {estado} com {y}% dos votos.")
                total_votos_candidato2 += delegados
                votos_populares2 += votos_candidato2
    # print(estado)
    # print(delegados)

if total_votos_candidato1 > total_votos_candidato2:
    vencedor = candidato_1
    print(f'Temos o resultado final! {vencedor} vence a disputa pela presidência, com o apoio de {total_votos_candidato1} delegados do colégio eleitoral e {votos_populares1} votos populares.')
    if candidato_2 == "Kanye West":
        print("\"Não tem problema, eu obtive o molho!\"")
    elif candidato_1 == "Kanye West":
        print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")
elif total_votos_candidato2 > total_votos_candidato1:
    vencedor = candidato_2
    print(f'Temos o resultado final! {vencedor} vence a disputa pela presidência, com o apoio de {total_votos_candidato2} delegados do colégio eleitoral e {votos_populares2} votos populares.')
    if candidato_1 == "Kanye West":
        print("\"Não tem problema, eu obtive o molho!\"")
    elif candidato_2 == "Kanye West":
        print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")