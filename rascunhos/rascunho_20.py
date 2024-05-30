qtd_musicas = int(input("Quantas músicas? "))

for _ in range(qtd_musicas):
    musica = input("Digite o nome da música: ")
    
    # Construir a string `forca` com espaços e sublinhados sem usar listas
    forca = ""
    for char in musica:
        if char == ' ':
            forca += ' '
        else:
            forca += '_'

    while '_' in forca:
        chute = input("Digite uma letra: ")

        # Atualizar a string `forca` com o chute correto sem usar listas
        nova_forca = ""
        for i in range(len(musica)):
            if musica[i] == chute:
                nova_forca += chute
            else:
                nova_forca += forca[i]
        forca = nova_forca

        print(forca)