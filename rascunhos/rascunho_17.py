qtd_musicas = int(input())

for i in range(qtd_musicas):
    musica = input()
    forca = ""
    for a in musica:
        if a == ' ':
            forca += ' '
        else:
            forca += '_'

    while '_' in forca:
        chute = input()

        nova_forca = ""
        for i in range(len(musica)):
            if musica[i] == chute:
                nova_forca += chute
            else:
                nova_forca += forca[i]
        forca = nova_forca

        for x in forca:
            print(x, end="")
        print()