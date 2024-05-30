# Atividade 9 da Lista 2

# Output exigido pelo desafio
print("Bem vindo ao jogo da forca do ye!")

# Input exigido pelo desafio
# Definição de quantidade de músicas que serão jogadas no jogo da Forca
qtd_musicas = int(input())
# Variável de apoio para zerar a pontuação (quantidade de músicas totalmente desvendadas)
total_pontos = 0

# Loop principal que faz o jogo funcionar
for i in range(qtd_musicas):
    # Definição da música
    musica = input()
    # Condição para definir se é a música 'N' ou a última música
    if (i + 1) != qtd_musicas:
        print(f"Esta é a música {i + 1} de {qtd_musicas}.")
    elif (i + 1) == qtd_musicas:
        print(f"Última música!")
    
    # Variável de apoio, criando uma variável "forca" vazia e outra resetando o número de letras de cada música
    forca = ""
    num_letras = 0

    # Construção da palavra escondida, substituindo as letras por underscores
    for a in musica:
        # Se o caractere analisado no momento for um espaço vazio, então deve adicionar um espaço na palavra escondida
        if a == ' ':
            forca += ' '
        # Caso não, adicionar underscores
        else:
            forca += '_'
            # Conta quantidade de letras da palavra, ignorando o espaço vazio
            num_letras += 1
    
    # Variável de apoio para armazenar o número de tentativas disponíveis para o usuário
    tentativas = num_letras * 2

    # Variável de apoio armazenando vazio para posteriormente receber todas as letras já chutadas pelo usuário
    chutes_de_antes = ""

    # Loop que analisa se a palavra escondida ainda possui underscores e se as tentativas ainda não zeraram
    while '_' in forca and tentativas > 0:
        # Input exigido pelo desafio, chute de alguma letra
        chute = input()
        # Caso a letra já tenha sido chutada, então o output será este
        if chute in chutes_de_antes:
            print("Já tinha colocado essa letra antes, preciso de mais atenção.")
            tentativas -= 1
        # Caso não, o cálculo continua
        else:
            # A letra chutada é armazenada na respectiva variável
            chutes_de_antes += chute

            # Variável de apoio para auxiliar na criação da forca
            nova_forca = ""
            # Variável que armazena se o usuário acertou a letra chutada
            acertou_letra = False # Falsa por padrão

            # Loop para criar a forca de acordo com as letras acertas
            # Para b na quantidade de letras da música
            for b in range(len(musica)):
                # Se o caractere da música analisado na ordem do Loop for igual ao chute, então adiciona o caractere na nova forca
                if musica[b] == chute:
                    nova_forca += chute
                    # O acerto de letra vira verdadeiro
                    acertou_letra = True
                else:
                    # Caso não, adiciona-se o caractere que já estava na primeira variável da forca (que pode ser ou um underscore ou um caractrre já acertado)
                    nova_forca += forca[b] #forca[b]
            
            # Variável de organização
            forca = nova_forca

            # Condição para output se acertou o caractere ou não
            if acertou_letra:
                print("Uhuuuuu! Consegui adivinhar uma letra!")
            else:
                print(f"Eita! Parece que a letra {chute} não está na música secreta!")
                
            tentativas -= 1
            
            # Print da situação atual do jogo
        print(f"Resposta atual: {forca}")

    # Condição para definir se acertou a música ou não
    if '_' not in forca:
        print("Isso! Consegui acertar uma música!")
        total_pontos += 1
    else:
        print(f"Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!")

# Output exigido pelo desafio
print(f"Consegui acertar {total_pontos} músicas de {qtd_musicas}!")

# Cálculo de porcentagem de acerto das músicas
taxa_acertos = (total_pontos / qtd_musicas) * 100

# Output exigido pelo desafio
if taxa_acertos == 100:
    print("Eu sou o próprio Kanye West.")
elif taxa_acertos > 75:
    print("Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.")
elif taxa_acertos > 50:
    print("Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.")
else:
    print("Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!")