# Atividade 8 da Lista 2

# Inputs exigidos pelo desafio + variáveis de apoio
candidato_1 = input()
candidato_2 = input()
votos_populares1 = 0
votos_populares2 = 0
total_votos_candidato1 = 0
total_votos_candidato2 = 0
urna = True

# Variável com texto armazenado para evitar erros de sintaxe
taylor_roubou = "Taylor Swift roubou as urnas!"

# Loop para manter votação ativa
while urna:
    # Condição para definir se o loop quebrará ou continuará
    if candidato_1 != "Kanye West" and candidato_2 != "Kanye West":
        # Nesse caso, caso não haja Kanye West, a votação é encerrada
        print("Sem o Ye, sem eleição!")
        urna = False
    else:
        # Votação completa com a presença do Kanye West
        # Input exigido pelo desafio
        conjunto = input()
        # Condição para manter a votação ativa
        if conjunto == "FIM":
            urna = False
        elif conjunto != "FIM" and urna:
            # Uso do método .split() para separar texto em 'N' strings
            x = conjunto.split(", ")
            estado, delegados = x
            delegados = int(delegados)
            votos_candidato1 = input()
            if votos_candidato1 != taylor_roubou:
                votos_candidato2 = input()
            # Caso a Taylor Swift roube a urna, a votação é reiniciada no estado
            while votos_candidato1 == taylor_roubou or votos_candidato2 == taylor_roubou:
                print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                votos_candidato1 = input()
                if votos_candidato1 != taylor_roubou:
                    votos_candidato2 = input()
            votos_candidato1 = int(votos_candidato1)
            votos_candidato2 = int(votos_candidato2)
            total_estado = votos_candidato1 + votos_candidato2
            # Condição para definir qual candidato obteve maior porcentagem no estado
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

# Condições para definir o output final
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