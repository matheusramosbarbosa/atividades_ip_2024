# Atividade 9 da Lista 2

print("Bem vindo ao jogo da forca do ye!")

qtd_musicas = int(input())
total_pontos = 0

for i in range(qtd_musicas):
    musica = input()
    if (i + 1) != qtd_musicas:
        print(f"Esta é a música {i + 1} de {qtd_musicas}.")
    else:
        print(f"Última música!")
    forca = ""
    num_letras = 0

    for a in musica:
        if a == ' ':
            forca += ' '
        else:
            forca += '_'
            num_letras += 1
        
    tentativas = num_letras * 2
    chutes_de_antes = ""

    while '_' in forca and tentativas > 0:
        chute = input()

        if chute in chutes_de_antes:
            print("Já tinha colocado essa letra antes, preciso de mais atenção.")
            tentativas -= 1
        else:
            chutes_de_antes += chute

            nova_forca = ""
            acertou_letra = False

            for b in range(len(musica)):
                if musica[b] == chute:
                    nova_forca += chute
                    acertou_letra = True
                else:
                    nova_forca += forca[b]

            forca = nova_forca

            if acertou_letra:
                print("Uhuuuuu! Consegui adivinhar uma letra!")
            else:
                print(f"Eita! Parece que a letra {chute} não está na música secreta!")

            tentativas -= 1
            
        print(f"Resposta atual: {forca}")

    if '_' not in forca:
        print("Isso! Consegui acertar uma música!")
        total_pontos += 1
    else:
        print(f"Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!")

print(f"Consegui acertar {total_pontos} músicas de {qtd_musicas}!")

taxa_acertos = (total_pontos / qtd_musicas) * 100

if taxa_acertos == 100:
    print("Eu sou o próprio Kanye West.")
elif taxa_acertos > 75:
    print("Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.")
elif taxa_acertos > 50:
    print("Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.")
else:
    print("Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!")
