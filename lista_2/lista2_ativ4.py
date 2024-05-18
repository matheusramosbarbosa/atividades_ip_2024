# Atividade 4 da Lista 2

quantidade_exercicios = int(input())
treino = True
maior_7 = 0
menor_7 = 0
# treino_perna = "TREINO DE PERNA DEUS DAI ME FORCAS"
# treino_costas = "TREINO DE COSTAS FE EM DEUS QUE VAI"
# treino_peito = "TREINO DE PEITO AMEM SENHOR"
fim = "Fim do Treino"


while treino:
    tipo_treino = input()
    if tipo_treino != "Fim do Treino":
        contagem = 1
        print(f'{tipo_treino}')
        for i in range (quantidade_exercicios):
            nome_musica = input()
            nota_musica = int(input())
            print(f'{contagem}° música {nome_musica} tocando agora')
            contagem += 1
            if nota_musica >= 7:
                print("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
                maior_7 += 1
            elif nota_musica < 7:
                print("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")
                menor_7 += 1
        if (quantidade_exercicios % 2 == 1) and maior_7 >= ((quantidade_exercicios + 1) // 2):
            print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
        elif (quantidade_exercicios % 2 == 0) and maior_7 >= (quantidade_exercicios // 2):
            print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
        else:
            print("NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL")
        maior_7 = 0
        menor_7 = 0
    elif tipo_treino == "Fim do Treino":
        treino = False
        quantidade_exercicios = 0
