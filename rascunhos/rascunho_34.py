# Atividade 10 da Lista 3

vazio = '*'
pedra = 'p'
carvao = 'a'
cobre = 'c'
ferro = 'f'
ouro = 'o'
barril = 'b'
escada = 'e'
tag_item = ['p', 'a', 'c', 'f', 'o']
valores_atuais = [0, 0, 0, 0, 0]
inventario = []

# Inputs exigidos pelo desafio
picareta = input()
if picareta == 'basica':
    lista_picareta = [pedra, carvao, cobre, barril]
elif picareta == 'cobre':
    lista_picareta = [pedra, carvao, cobre, barril, ferro]
elif picareta == 'ferro':
    lista_picareta = [pedra, carvao, cobre, barril, ferro, ouro]

mochila = input()
if mochila == 'basica':
    qtd_mochila = 10
elif mochila == 'media':
    qtd_mochila = 20
elif mochila == 'grande':
    qtd_mochila = 30

comida = input()

lista_comida = comida.split(' - ')
nome_comida = lista_comida.pop(0)

for i in range(len(lista_comida)):
    lista_comida[i] = int(lista_comida[i])

if lista_comida[0] == 1:
    print(f'Hoje, irei levar apenas uma unidade de {nome_comida}.')
elif lista_comida[0] > 1:
    print(f'Bom estoque! vou levar {lista_comida[0]} unidades de {nome_comida}.')
else:
    print(f'Vai ser tenso, vou levar nada pra repor minha energia...')

inventario.append('picareta')
if nome_comida != 'nenhuma':
    inventario.append(nome_comida)


andares = int(input())
energia = 100
na_mina = True
parada = False
andar_atual = 0

while andares > 0 and not parada:
    qtd_barris = []
    energia_gasta = 0
    tam = input()
    lista_tam = tam.split(' ')
    matriz_principal = []

    for i in range(len(lista_tam)):
        lista_tam[i] = int(lista_tam[i])
    
    if lista_tam[0] == lista_tam[1]:
        print(f'Poxa! Esse andar é um quadrado perfeito de lado {lista_tam[0]}!!!')
    else:
        print(f'Esse andar da caverna parece um retângulo ou uma matriz {lista_tam[0]}x{lista_tam[1]}. Depois de minerar, ela ficou assim:')
    
    for i in range (lista_tam[0]):
        matriz_principal.append([])
    
    for i in range (lista_tam[0]):
        matriz_do_usuario = input()
        matriz_aux = matriz_do_usuario.split(' ')
        for a in matriz_aux:
            matriz_principal[i].append(a)

    for i in range (len(matriz_principal)):
        for a in range (len(matriz_principal[i])):
            if matriz_principal[i][a] == barril:
                qtd_barris.append('b')
        
        for a in range (len(matriz_principal[i])):
            if matriz_principal[i][a] in lista_picareta:
                if matriz_principal[i][a] in inventario:
                    if matriz_principal[i][a] in tag_item:
                        aux = tag_item.index(matriz_principal[i][a])
                        valores_atuais[aux] += 1
                else:
                    if matriz_principal[i][a] != 'b':
                        inventario.append(matriz_principal[i][a])
                        if matriz_principal[i][a] in tag_item:
                            aux = tag_item.index(matriz_principal[i][a])
                            valores_atuais[aux] += 1
                matriz_principal[i][a] = '*'
                energia_gasta += 3

    for i in matriz_principal:
        aux2 = ' '.join(i)
        print(aux2)
            
    for d in range(len(qtd_barris)):
            itens_bau_temp = input()
            lista_itens_bau = itens_bau_temp.split(', ')
            if 'rubi' in lista_itens_bau:
                if len(inventario) < qtd_mochila:
                    if 'rubi' not in inventario:
                        inventario.append('rubi')
                        print(f'MEU DEUS EU ACHEI UM RUBI NESSE BARRIL!!!')
            else:
                for b in lista_itens_bau:
                    if len(inventario) < qtd_mochila:
                        if b == nome_comida:
                            lista_comida[0] += 1
                        if b not in inventario:
                            inventario.append(b)
                print(f'Opa, quebrei o {d + 1}º barril e recebi {len(lista_itens_bau)} itens.')
    
    andares -= 1
    andar_atual += 1
    energia -= energia_gasta

    while energia <= 10 and lista_comida[0] > 0:
        lista_comida[0] -= 1
        energia += lista_comida[1]
    
    if lista_comida == 0:
        if nome_comida in inventario:
            inventario.remove(nome_comida)

    if andares == 0:
        print(f'Cheguei aonde eu queria por hoje, vou sair.')
    elif energia <= 10:
        print(f'To sem energia para continuar minerando. Pelo menos cheguei ao andar {andar_atual}.')
        parada = True
    else:
        print(f'Ainda dá pra continuar minerando, vamos simbora!!!')

print(f'Pronto, acabei de sair da mina. Vamos ver o que eu consegui:')
print(f'Total de pedra: {valores_atuais[0]}.')
print(f'Total de carvão: {valores_atuais[1]}.')
print(f'Total de cobre: {valores_atuais[2]}.')
print(f'Total de ferro: {valores_atuais[3]}.')
print(f'Total de ouro: {valores_atuais[4]}.')

if len(inventario) == qtd_mochila:
    print(f'A bolsa volta cheia hoje :)')

if 'rubi' in inventario:
    print(f'A mineração hoje foi incrível!!!')
else:
    print(f'A mineração foi boa, mas ainda estão falando que roubei os melões :(')
