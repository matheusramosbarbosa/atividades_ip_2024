salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
salas_feitas = ["caldeira", "aquário", "mural"]

# Copa
conjuntos_da_copa = ['recursos da primavera', 'recursos doa verao', 'recursos do outono', 'recursos do inverno']
itens_da_copa = [["raiz-forte", "narciso", "alho-poro", "dente-de-leao"], ["uva", "cafe-de-jardim", "ervilha-de-cheiro"], ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"], ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]]

# Artesanato
conjuntos_do_artesanato = ['plantacoes da primavera', 'plantacoes do verao', 'plantacoes do outono', 'artesao']
itens_do_artesanato = [["chirivia", "vagem", "couve-flor", "batata"], ["tomate", "mirtilo", "melao", "pimenta-quente"], ["milho", "beringela", "abobora", "inhame"], ["mel", "geleia", "queijo", "tecido"]]

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
    repeticoes = []
    lista_aux = []
    lista_aux_2 = []

    conjuntos = input()
    lista_conjuntos = conjuntos.split(', ')

    for d in lista_conjuntos:
        if d in lista_aux:
            repeticoes.append(d)
        else:
            lista_aux.append(d)
    
    lista_conjuntos = lista_aux

    itens_bau = input()
    lista_itens_bau = itens_bau.split(', ')

    for e in lista_itens_bau:
        if e in lista_aux_2:
            repeticoes.append(e)
        else:
            lista_aux_2.append(e)
    
    lista_itens_bau = lista_aux_2


    # for i in lista_itens_bau:
    #     if i == "":
    #         lista_itens_bau.remove(i)
    #     elif i == " ":
    #         lista_itens_bau.remove(i)


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
                if sala == 'copa':
                    for a in range(len(lista_conjuntos)):
                        if lista_conjuntos[a] in conjuntos_da_copa:
                            aux = conjuntos_da_copa.index(lista_conjuntos[a]) 
                            todos_itens = todos_itens + itens_da_copa[aux]
                elif sala == 'artesanato':
                    for b in range(len(lista_conjuntos)):
                        if lista_conjuntos[b] in conjuntos_da_copa:
                            aux = conjuntos_do_artesanato.index(lista_conjuntos[b]) 
                            todos_itens = todos_itens + itens_do_artesanato[aux]
                for i in lista_itens_bau:
                    if i in todos_itens:
                        print(f'{i} vai ser entregue ao centro logo!')
                    else:
                        print(f'{i} pode ser analisado depois')
                if len(repeticoes) > 0:
                    print(f'Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')
                esqueceu = True

