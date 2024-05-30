# Atividade 10 da Lista 2

num_rodadas = int(input())
pontos_taylor = 0
pontos_kanye = 0
pontos_desordem_kanye = 0
pontos_desordem_taylor = 0
descontentamento = True
pontos_rodada_kanye = 0
pontos_rodada_taylor = 0


for i in range(num_rodadas):
    print(f"{i + 1}° RODADA:")
    if pontos_desordem_kanye < 5 and pontos_desordem_taylor < 5:
        musica = input()
        pontos_kanye = 0
        for a in range(3):
            avaliacao = input()
            if avaliacao == "boa":
                pontos_kanye += 2
            elif avaliacao == "média":
                pontos_kanye += 1
            elif avaliacao == "ruim":
                pontos_kanye -= 3
            elif avaliacao == "péssima":
                while descontentamento:
                    frase_descontentamento = input()
                    if frase_descontentamento == "ORDEM":
                        descontentamento = False
                    elif frase_descontentamento != "":
                        pontos_desordem_kanye += 1
                descontentamento = True
            
        if pontos_desordem_kanye < 5:
            musica = input()
            pontos_taylor = 0
            for a in range(3):
                avaliacao = input()
                if avaliacao == "boa":
                    pontos_taylor += 2
                elif avaliacao == "média":
                    pontos_taylor += 1
                elif avaliacao == "ruim":
                    pontos_taylor-= 3
                elif avaliacao == "péssima":
                    while descontentamento:
                        frase_descontentamento = input()
                        if frase_descontentamento == "ORDEM":
                            descontentamento = False
                        elif frase_descontentamento != "":
                            pontos_desordem_kanye += 1
                    descontentamento = True
    if pontos_kanye > pontos_taylor and pontos_desordem_kanye < 5 and pontos_desordem_taylor < 5:
        print(f"O(a) vencedor(a) da {i + 1}° rodada foi Kanye West")
        pontos_rodada_kanye += 1
    elif pontos_taylor > pontos_kanye and pontos_desordem_taylor < 5 and pontos_desordem_kanye < 5:
        print(f"O(a) vencedor(a) da {i + 1}° rodada foi Taylor Swift")
        pontos_rodada_taylor += 1
    elif pontos_taylor == pontos_kanye and pontos_desordem_taylor < 5 and pontos_desordem_kanye < 5:
        print(f"Não houve vencedor na {i + 1}° rodada")

    if pontos_rodada_kanye >= 3:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {pontos_rodada_kanye} vitórias, é Kanye West, parabéns!")
        num_rodadas = 0
    elif pontos_rodada_taylor >= 3:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {pontos_rodada_taylor} vitórias, é Taylor Swift, parabéns!")
        num_rodadas = 0

if pontos_rodada_taylor < 3 and pontos_rodada_kanye < 3:
    if pontos_desordem_kanye >= 5:
                print(f"Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!")
                print(f"O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!")
    elif pontos_desordem_taylor >= 5:
                print(f"Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!")
                print(f"O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!")
    elif pontos_rodada_kanye > pontos_rodada_taylor and pontos_desordem_kanye < 5:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {pontos_rodada_kanye} vitórias, é Kanye West, parabéns!")
    elif pontos_rodada_taylor > pontos_rodada_kanye and pontos_desordem_taylor < 5:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {pontos_rodada_taylor} vitórias, é Taylor Swift, parabéns!")
    elif pontos_rodada_taylor == pontos_rodada_kanye and pontos_desordem_taylor < 5 and pontos_desordem_kanye < 5:
        print("Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!")