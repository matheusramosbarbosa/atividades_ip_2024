musica = input()
forca = ['_' for a in musica]

while '_' in forca:
    chute = input()

    for x in forca:
        print(x, end="")
    print()

    for i in range(len(musica)):
        if musica[i] == chute:
            forca[i] = chute

    for x in forca:
        print(x, end="")
    print()