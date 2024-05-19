# Atividade 10 da Lista 2

num_rodadas = int(input())
pontos_taylor = 0
pontos_kanye = 0
pontos_desordem_kanye = 0
pontos_desordem_taylor = 0
descontentamento = True
perdedor = ""
pontos_rodada_kanye = 0
pontos_rodada_taylor = 0

for i in range(num_rodadas):

    print(f"{i + 1}° RODADA:")

    musica_kanye = input()
    avaliacao_kanye1 = input()
    avaliacao_kanye2 = input()
    avaliacao_kanye3 = input()

    if avaliacao_kanye1 == "boa":
        pontos_kanye += 2
    elif avaliacao_kanye1 == "média":
        pontos_kanye += 1
    elif avaliacao_kanye1 == "ruim":
        pontos_kanye -= 3
    elif avaliacao_kanye1 == "péssima":
        while descontentamento:
            frase_descontentamento = input()
            if frase_descontentamento == "ORDEM":
                descontentamento = False
            elif frase_descontentamento != "":
                pontos_desordem_kanye += 1
    
    if avaliacao_kanye2 == "boa":
        pontos_kanye += 2
    elif avaliacao_kanye2 == "média":
        pontos_kanye += 1
    elif avaliacao_kanye2 == "ruim":
        pontos_kanye -= 3
    elif avaliacao_kanye2 == "péssima":
        while descontentamento:
            frase_descontentamento = input()
            if frase_descontentamento == "ORDEM":
                descontentamento = False
            elif frase_descontentamento != "":
                pontos_desordem_kanye += 1

    if avaliacao_kanye3 == "boa":
        pontos_kanye += 2
    elif avaliacao_kanye3 == "média":
        pontos_kanye += 1
    elif avaliacao_kanye3 == "ruim":
        pontos_kanye -= 3
    elif avaliacao_kanye3 == "péssima":
        while descontentamento:
            frase_descontentamento = input()
            if frase_descontentamento == "ORDEM":
                descontentamento = False
            elif frase_descontentamento != "":
                pontos_desordem_kanye += 1
     
    musica_taylor = input()
    avaliacao_taylor1 = input()
    avaliacao_taylor2 = input()
    avaliacao_taylor3 = input()

    if avaliacao_taylor1 == "boa":
        pontos_taylor += 2
    elif avaliacao_taylor1 == "média":
        pontos_taylor += 1
    elif avaliacao_taylor1 == "ruim":
        pontos_taylor -= 3
    elif avaliacao_taylor1 == "péssima":
        while descontentamento:
            frase_descontentamento = input()
            if frase_descontentamento == "ORDEM":
                descontentamento = False
            elif frase_descontentamento != "":
                pontos_desordem_taylor += 1

    if avaliacao_taylor2 == "boa":
        pontos_taylor += 2
    elif avaliacao_taylor2 == "média":
        pontos_taylor += 1
    elif avaliacao_taylor2 == "ruim":
        pontos_taylor -= 3
    elif avaliacao_taylor2 == "péssima":
        while descontentamento:
            frase_descontentamento = input()
            if frase_descontentamento == "ORDEM":
                descontentamento = False
            elif frase_descontentamento != "":
                pontos_desordem_taylor += 1

    if avaliacao_taylor3 == "boa":
        pontos_taylor += 2
    elif avaliacao_taylor3 == "média":
        pontos_taylor += 1
    elif avaliacao_taylor3 == "ruim":
        pontos_taylor -= 3
    elif avaliacao_taylor3 == "péssima":
        while descontentamento:
            frase_descontentamento = input()
            if frase_descontentamento == "ORDEM":
                descontentamento = False
            elif frase_descontentamento != "":
                pontos_desordem_taylor += 1

    if pontos_kanye > pontos_taylor and pontos_desordem_kanye < 5:
        print(f"O(a) vencedor(a) da {i + 1}° rodada foi Kanye West")
        pontos_rodada_kanye += 1
    elif pontos_taylor > pontos_kanye and pontos_desordem_taylor < 5:
        print(f"O(a) vencedor(a) da {i + 1}° rodada foi Taylor Swift")
        pontos_rodada_taylor += 1
    elif pontos_taylor == pontos_kanye and pontos_desordem_taylor < 5 and pontos_desordem_kanye < 5:
        print(f"Não houve vencedor na {i + 1}° rodada")

    #avaliações podem ser boa, média, ruim ou péssima

