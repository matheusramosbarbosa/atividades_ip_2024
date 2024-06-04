salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
salas_feitas = ["caldeira", "aquário", "mural"]

# Copa
conjuntos_da_copa = ['recursos da primavera', 'recursos do verao', 'recursos do outono', 'recursos do inverno']
itens_da_copa = [["raiz-forte", "narciso", "alho-poro", "dente-de-leao"], ["uva", "cafe-de-jardim", "ervilha-de-cheiro"], ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"], ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]]

# Artesanato
conjuntos_do_artesanato = ['plantacoes da primavera', 'plantacoes do verao', 'plantacoes do outono', 'artesao']
itens_do_artesanato = [["chirivia", "vagem", "couve-flor", "batata"], ["tomate", "mirtilo", "melao", "pimenta-quente"], ["milho", "beringela", "abobora", "inhame"], ["mel", "geleia", "queijo", "tecido"]]

completou = False
esta_no_centro = True

sala = input()

# Condição para definir se a sala escolhida existe realmente no centro
if sala in salas:
    # Condição para definir se a sala já foi completa ou não
    if sala in salas_feitas:
        completou = True
    else:
        completou = False
else:
    esta_no_centro = False


todos_itens = []
ja_utilizados = []
repeticoes = []
lista_aux = []
lista_aux_2 = []

conjuntos = input()
lista_conjuntos1 = conjuntos.split(', ')

for d in lista_conjuntos1:
    if d in lista_aux:
        repeticoes.append(d)
    else:
        lista_aux.append(d)

lista_conjuntos = lista_aux

itens_bau = input()
lista_itens_bau1 = itens_bau.split(', ')

for e in lista_itens_bau1:
    if e in lista_aux_2:
        repeticoes.append(e)
    else:
        lista_aux_2.append(e)

lista_itens_bau = lista_aux_2


if not esta_no_centro:
    print(f'Essa sala não está no centro comunitário')
else:
    if completou:
        print(f'Eu já conclui {sala}, não precisa doar mais itens para essa sala')
    elif "" in lista_itens_bau1 or " " in lista_itens_bau1 or "" in lista_conjuntos1 or " " in lista_conjuntos1:
        print('Sérgio esqueceu algumas informações, será que ele pode enviar novamente?')
    else:
        if sala == 'copa':
            for a in lista_conjuntos:
                if a in conjuntos_da_copa:
                    aux = conjuntos_da_copa.index(a) 
                    todos_itens += itens_da_copa[aux]
        elif sala == 'artesanato':
            for b in lista_conjuntos:
                if b in conjuntos_do_artesanato:
                    aux = conjuntos_do_artesanato.index(b) 
                    todos_itens += itens_do_artesanato[aux]

        for i in lista_itens_bau:
            if i in todos_itens:
                print(f'{i} vai ser entregue ao centro logo!')
            else:
                print(f'{i} pode ser analisado depois')
        if len(repeticoes) > 0:
            print(f'Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')
        esqueceu = True

