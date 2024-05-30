# Atividade 4 da Lista 2

# Inputs exigidos pelo desafio + variáveis de apoio
quantidade_exercicios = int(input())
treino = True
maior_7 = 0
menor_7 = 0

# Variável com texto para evitar erros na sintaxe da condição
fim = "Fim do Treino"


# Loop exigido pelo desafio
while treino:
    # Definição do tipo de treino (não altera em nada na condição se for diferente de "Fim do Treino")
    tipo_treino = input()
    # Condição para definir se o loop deve parar ou continuar
    if tipo_treino != "Fim do Treino":
        contagem = 1
        print(f'{tipo_treino}')
        # Loop que repete a quantidade de vezes de quantidade de exercícios
        for i in range (quantidade_exercicios):
            # Inputs e outputs pelo desafio
            nome_musica = input()
            nota_musica = int(input())
            print(f'{contagem}° música {nome_musica} tocando agora')
            contagem += 1
            # Condição para printar avaliação da música
            if nota_musica >= 7:
                print("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
                maior_7 += 1
            elif nota_musica < 7:
                print("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")
                menor_7 += 1
        # Sintaxe exigida pela OBS 4
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