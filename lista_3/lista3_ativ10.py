# Atividade 10 da Lista 3

# Variáveis que armazenam textos para evitar erros nas sintaxes das condições
vazio = '*'
pedra = 'p'
carvao = 'a'
cobre = 'c'
ferro = 'f'
ouro = 'o'
barril = 'b'
escada = 'e'

# Lista que contém os itens que devem ser apresentados no final do programa
tag_item = ['p', 'a', 'c', 'f', 'o']
# E seus respectivos valores
valores_atuais = [0, 0, 0, 0, 0]
# Lista que irá receber os itens do inventário
inventario = []

# Inputs exigidos pelo desafio
# Cada tipo de picareta recebe uma lista do que pode quebrar
picareta = input()
if picareta == 'basica':
    lista_picareta = [pedra, carvao, cobre, barril]
elif picareta == 'cobre':
    lista_picareta = [pedra, carvao, cobre, barril, ferro]
elif picareta == 'ferro':
    lista_picareta = [pedra, carvao, cobre, barril, ferro, ouro]

# Cada tipo de bolsa recebe um valor máximo de quantidade de itens que suporta
mochila = input()
if mochila == 'basica':
    qtd_mochila = 10
elif mochila == 'media':
    qtd_mochila = 20
elif mochila == 'grande':
    qtd_mochila = 30

# Recebe a comida
comida = input()

# Transforma em lista
lista_comida = comida.split(' - ')
# Retira o nome da comida da lista e joga em uma variável à parte
nome_comida = lista_comida.pop(0)

# Transforma o resto dos valores string em int
for i in range(len(lista_comida)):
    lista_comida[i] = int(lista_comida[i])

# Condição para definir output exigido pelo desafio
if lista_comida[0] == 1:
    print(f'Hoje, irei levar apenas uma unidade de {nome_comida}.')
elif lista_comida[0] > 1:
    print(f'Bom estoque! vou levar {lista_comida[0]} unidades de {nome_comida}.')
else:
    print(f'Vai ser tenso, vou levar nada pra repor minha energia...')

# Adiciona a picareta e a comida no inventário
inventario.append('picareta')
if nome_comida != 'nenhuma':
    inventario.append(nome_comida)

# Input exigido pelo desafio que recebe a quantidade de andares da mina
andares = int(input())

# Variáveis de apoio
energia = 100
na_mina = True
parada = False
andar_atual = 0

# Enquanto ainda existirem andares e o jogador não parar, o programa continua
while andares > 0 and not parada:

    # Variáveis de apoio
    qtd_barris = []
    energia_gasta = 0

    # Input exigido pelo desafio, recebe o tamanho da matriz (mina) no formato 'X Y'
    tam = input()
    lista_tam = tam.split(' ')

    # Lista principal do jogo, que recebe a matriz
    matriz_principal = []

    # Transforma os elementos do tamanho da matriz em int
    for i in range(len(lista_tam)):
        lista_tam[i] = int(lista_tam[i])
    
    # Se as colunas forem iguais às linhas, printa um output exigido pelo desafio, caso contrário, printa outro
    if lista_tam[0] == lista_tam[1]:
        print(f'Poxa! Esse andar é um quadrado perfeito de lado {lista_tam[0]}!!!')
    else:
        print(f'Esse andar da caverna parece um retângulo ou uma matriz {lista_tam[0]}x{lista_tam[1]}. Depois de minerar, ela ficou assim:')
    
    # Adiciona as linhas na matriz principal
    for i in range(lista_tam[0]):
        matriz_principal.append([])
    
    # Recebe a matriz do usuário por linha
    for i in range(lista_tam[0]):
        matriz_do_usuario = input()
        matriz_aux = matriz_do_usuario.split(' ')
        for a in matriz_aux:
            matriz_principal[i].append(a)
            
    # Para cada barril recebido, os adiciona numa lista nova para ajudar na construção da lógica (não os retira da matriz ainda)
    for i in range(len(matriz_principal)):
        for a in range(len(matriz_principal[i])):
            if matriz_principal[i][a] == barril:
                qtd_barris.append('b')
        
        # Adiciona o item no contador de itens exigidos no print final e no inventário, e minera o item da matriz, retirando-o e substituindo por um asterisco
        for a in range(len(matriz_principal[i])):
            if matriz_principal[i][a] in lista_picareta:
                # Se não estiver no inventário, adiciona o item no inventário
                if matriz_principal[i][a] in inventario:
                    if matriz_principal[i][a] in tag_item:
                        aux = tag_item.index(matriz_principal[i][a])
                        valores_atuais[aux] += 1
                else:
                    # Só minerea se 
                    if matriz_principal[i][a] != 'b':
                        inventario.append(matriz_principal[i][a])
                        if matriz_principal[i][a] in tag_item:
                            aux = tag_item.index(matriz_principal[i][a])
                            valores_atuais[aux] += 1
                matriz_principal[i][a] = '*'
                energia_gasta += 3 # Contador de gasto de energia

    # Printa a mina
    for i in matriz_principal:
        aux2 = ' '.join(i)
        print(aux2)

    # Verifica se encontrou um rubi em cada barril encontrado (caso tenha encontrado barris)            
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
    

    # Antes de ir para o próximo andar:

    # Retira um andar do contador
    andares -= 1
    # Adiciona um andar no contador do andar atual
    andar_atual += 1
    # Retira a energia gasta pelo jogador
    energia -= energia_gasta

    # Enquanto a energia for menor ou igual a 10, come a comida (se o jogador estiver com comida)
    while energia <= 10 and lista_comida[0] > 0:
        lista_comida[0] -= 1
        energia += lista_comida[1]
    
    # Se a comida acabar, remove ela do inventário
    if lista_comida[0] == 0 and nome_comida != 'nenhuma':
        if nome_comida in inventario:
            inventario.remove(nome_comida)
    
    # Se os andares acabarem, jogador vai embora e loop termina
    if andares == 0:
        print(f'Cheguei aonde eu queria por hoje, vou sair.')
    # Se, mesmo após comer (ou não), a energia for menor ou igual a 10, o usuário vai embora e o loop termina
    elif energia <= 10:
        print(f'To sem energia para continuar minerando. Pelo menos cheguei ao andar {andar_atual}.')
        parada = True
    # Se não, vai para o próximo andar
    else: 
        print(f'Ainda dá pra continuar minerando, vamos simbora!!!')

# Outputs exigidos pelo desafio
print(f'Pronto, acabei de sair da mina. Vamos ver o que eu consegui:')
print(f'Total de pedra: {valores_atuais[0]}.')
print(f'Total de carvão: {valores_atuais[1]}.')
print(f'Total de cobre: {valores_atuais[2]}.')
print(f'Total de ferro: {valores_atuais[3]}.')
print(f'Total de ouro: {valores_atuais[4]}.')

# Printa output exigido pelo desafio caso o inventário esteja cheio
if len(inventario) == qtd_mochila:
    print(f'A bolsa volta cheia hoje :)')

# Output final exigido pelo desafio
if 'rubi' in inventario:
    print(f'A mineração hoje foi incrível!!!')
else:
    print(f'A mineração foi boa, mas ainda estão falando que roubei os melões :(')
