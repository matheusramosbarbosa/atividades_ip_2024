# Atividade 7 da Lista 3

tam_lista = input()
lista_aux = tam_lista.split(' x ')
for a in range(len(lista_aux)):
    lista_aux[a] = int(lista_aux[a])

lista_principal = []

linhas = lista_aux[0]
colunas = lista_aux[1]

for b in range(linhas):
    lista_principal.append([])

for c in lista_principal:
    for d in range(colunas):
        c.append(' ')


qtd_elementos = int(input())

for i in range(qtd_elementos):
    entrada = input()
    elemento, local = entrada.split(' ', 1)
    loc_def = ''
    for d in local:
        if d == '(' or d == ')':
            loc_def += ''
        else:
            loc_def += d
    local = loc_def.split(',')

    for e in range(len(local)):
        local[e] = int(local[e])

    lista_principal[local[0]][local[1]] = elemento

for f in range(len(lista_principal)):
    for g in range (len(lista_principal[f])):
        if lista_principal[f][g] == ' ':
            lista_principal[f][g] = '0'

calculo = True
while calculo:
    comando = input()
    if comando == "Permutar":
        permutacao = input()
        pos_antiga, pos_nova = permutacao.split(' ')
        pos_antiga_def = ''
        pos_nova_def = ''
        for h in pos_antiga:
            if h == '(' or h == ')':
                pos_antiga_def += ''
            else:
                pos_antiga_def += h
        for j in pos_nova:
            if j == '(' or j == ')':
                pos_nova_def += ''
            else:
                pos_nova_def += j
        pos1 = pos_antiga_def.split(',')
        for k in range(len(pos1)):
            pos1[k] = int(pos1[k])
        pos2 = pos_nova_def.split(',')
        for l in range(len(pos2)):
            pos2[l] = int(pos2[l])
        
        lista_principal[pos1[0]][pos1[1]], lista_principal[pos2[0]][pos2[1]] = lista_principal[pos2[0]][pos2[1]], lista_principal[pos1[0]][pos1[1]]
    elif comando == 'Transposição':
        nova_lista = []
        linhas, colunas = colunas, linhas
        for m in range(linhas):
            nova_lista.append([])
        for n in nova_lista:
            for o in range(colunas):
                n.append('')
        
        for p in range(len(nova_lista)):
            for q in range(len(nova_lista[p])):
                nova_lista[p][q] = lista_principal[q][p]

        lista_principal = nova_lista
    elif comando == 'Remover':
        menor = float('inf')  
        menor_pos = [0, 0]   
    
        for r in range(len(lista_principal)):
            for s in range(len(lista_principal[r])):
                if lista_principal[r][s] != '0':
                    valor_atual = int(lista_principal[r][s])
                    if valor_atual < menor:
                        menor = valor_atual
                        menor_pos = [r, s]

        lista_principal[menor_pos[0]][menor_pos[1]] = '0'

    else:
        calculo = False

print('Atual Arranjo:')
for r in range(len(lista_principal)):
    print(' '.join(lista_principal[r]))

# menor_elemento = float('inf')
#         menor_indice = -1
#         for r in range(len(lista_principal)):
#             for s in range(len(lista_principal[r])):
#                 if lista_principal[s][r] > 0 and lista_principal[s][r] < menor_elemento:
#                     menor_elemento = lista_principal[s][r]
                    