# Atividade 8 da Lista 3

# Todas as salas do centro
salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
# Salas completas por Sérgio
salas_feitas = ["caldeira", "aquário", "mural"]

# Copa
# Conjuntos da copa e seus respectivos itens
conjuntos_da_copa = ['recursos da primavera', 'recursos do verao', 'recursos do outono', 'recursos do inverno']
itens_da_copa = [["raiz-forte", "narciso", "alho-poro", "dente-de-leao"], ["uva", "cafe-de-jardim", "ervilha-de-cheiro"], ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"], ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]]

# Artesanato
# Conjuntos da sala de artesanato e seus respectivos itens
conjuntos_do_artesanato = ['plantacoes da primavera', 'plantacoes do verao', 'plantacoes do outono', 'artesao']
itens_do_artesanato = [["chirivia", "vagem", "couve-flor", "batata"], ["tomate", "mirtilo", "melao", "pimenta-quente"], ["milho", "beringela", "abobora", "inhame"], ["mel", "geleia", "queijo", "tecido"]]

# Variáveis de apoio
completou = False
esta_no_centro = True

# Input exigido pelo dasafio, recebe para qual sala o usuário quer enviar os itens
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

# Listas de apoio
todos_itens = []
ja_utilizados = []
repeticoes = []
lista_aux = []
lista_aux_2 = []

# Input exigido pelo desafio, recebe os conjuntos
conjuntos = input()
lista_conjuntos1 = conjuntos.split(', ')

# Loop que faz repetições serem evitadas na construção da lógica correta, joga as repetições numa lista auxiliar
for d in lista_conjuntos1:
    if d in lista_aux:
        repeticoes.append(d)
    else:
        lista_aux.append(d)

lista_conjuntos = lista_aux

# Input exigido pelo desafio, recebe os itens
itens_bau = input()
lista_itens_bau1 = itens_bau.split(', ')

# Loop que faz repetições serem evitadas na construção da lógica correta, joga as repetições numa lista auxiliar
for e in lista_itens_bau1:
    if e in lista_aux_2:
        repeticoes.append(e)
    else:
        lista_aux_2.append(e)

lista_itens_bau = lista_aux_2

# Se a sala não estiver no centro comunitário, uma mensagem é enviada e o programa termina
if not esta_no_centro:
    print(f'Essa sala não está no centro comunitário')
else:
    # Se a sala escolhida já estiver completa, uma mensagem é enviada e o programa termina
    if completou:
        print(f'Eu já conclui {sala}, não precisa doar mais itens para essa sala')
    # Se houver espaços ou itens em branco na lista, uma mensagem é enviada e o programa termina
    elif "" in lista_itens_bau1 or " " in lista_itens_bau1 or "" in lista_conjuntos1 or " " in lista_conjuntos1:
        print('Sérgio esqueceu algumas informações, será que ele pode enviar novamente?')
    # Se não, programa continua
    else:
        # Se a sala escolhida for a copa, então adicionamos numa lista que contém todos os itens que devem ser analisados, os itens do(s) conjunto(s) escolhido da copa
        if sala == 'copa':
            for a in lista_conjuntos:
                if a in conjuntos_da_copa:
                    aux = conjuntos_da_copa.index(a) 
                    todos_itens += itens_da_copa[aux]
        # Se a sala escolhida for a de artesanato, então adicionamos numa lista que contém todos os itens que devem ser analisados, os itens do(s) conjunto(s) escolhido da sala da copa
        elif sala == 'artesanato':
            for b in lista_conjuntos:
                if b in conjuntos_do_artesanato:
                    aux = conjuntos_do_artesanato.index(b) 
                    todos_itens += itens_do_artesanato[aux]

        # Análise de itens
        for i in lista_itens_bau:
            if i in todos_itens:
                print(f'{i} vai ser entregue ao centro logo!')
            else:
                print(f'{i} pode ser analisado depois')
        # Se tiver repetições, printar output exigido pelo desafio
        if len(repeticoes) > 0:
            print(f'Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')
        
        # Variável que define o fim do loop
        esqueceu = True

