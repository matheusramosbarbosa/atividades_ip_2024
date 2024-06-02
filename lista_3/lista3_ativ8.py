# Atividade 8 da Lista 3

salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
salas_feitas = ["caldeira", "aquário", "mural"]

# Copa
recursos_primavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursos_verão = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recursos_outono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recursos_inverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]

# Artesanato
plantacoes_primavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoes_verao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoes_outono = ["milho", "beringela", "abobora", "inhame"]
artesao = ["mel", "geleia", "queijo", "tecido"]

completou = False
esta_no_centro = True

sala = input()

# Condição para definir se a sala escolhida existe ralmente no centro
if sala in salas:
    # Condição para definir se a sala já foi completa ou não
    if sala in salas_feitas:
        completou = True
    else:
        completou = False
else:
    esta_no_centro = False

esqueceu = False

while not esqueceu:
    todos_itens = []
    ja_utilizados = []
    conjuntos = input()
    lista_conjuntos = conjuntos.split(', ')
    print(lista_conjuntos)

    itens_bau = input()
    lista_itens_bau = itens_bau.split(', ')
    print(lista_itens_bau)

    # for i in lista_itens_bau:
    #     if i == "":
    #         lista_itens_bau.remove(i)
    #     elif i == " ":
    #         lista_itens_bau.remove(i)

    print(lista_itens_bau)

    if esta_no_centro == False:
        print(f'Essa sala não está no centro comunitário')
        esqueceu = True
    else:
        if completou == True:
            print(f'Eu já conclui {sala}, não precisa doar mais itens para essa sala')
            esqueceu = True
        else:
            if "" in lista_itens_bau or " " in lista_itens_bau or "" in lista_conjuntos or " " in lista_conjuntos:
                print('Sérgio esqueceu algumas informações, será que ele pode enviar novamente?')
                esqueceu = False
            else:
                if sala == "copa":
                    if 'recursos da primavera' in lista_conjuntos:
                        todos_itens = todos_itens + recursos_primavera
                    if 'recursos do verao' in lista_conjuntos:
                        todos_itens = todos_itens + recursos_verão
                    if 'recursos do outono' in lista_conjuntos:
                        todos_itens = todos_itens + recursos_outono
                    if  'recursos do inverno' in lista_conjuntos:
                        todos_itens = todos_itens + recursos_inverno
                elif sala == "artesanato":
                    if 'plantacoes da primavera' in lista_conjuntos:
                        todos_itens = todos_itens + plantacoes_primavera
                    if 'plantacoes do verao' in lista_conjuntos:
                        todos_itens = todos_itens + plantacoes_verao
                    if 'plantacoes do outono' in lista_conjuntos:
                        todos_itens = todos_itens + plantacoes_outono
                    if 'artesao' in lista_conjuntos:
                        todos_itens = todos_itens + artesao
                for i in itens_bau:
                    if i in todos_itens:
                        print(f'{i} vai ser entregue ao centro logo!')
                        ja_utilizados.append[i]
                    else:
                        print(f'{i} pode ser analisado depois')
                        ja_utilizados.append[i]