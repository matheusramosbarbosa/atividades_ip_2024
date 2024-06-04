# Atividade 7 da Lista 3

# Input exigido pelo desafio, recebe tamanho da lista
tam_lista = input()
lista_aux = tam_lista.split(' x ') # Transforma em uma lista
# Transforma string em int
for a in range(len(lista_aux)):
    lista_aux[a] = int(lista_aux[a])

# Lista principal
lista_principal = []

# Variáveis de apoio que armazenam valores de colunas e linhas
linhas = lista_aux[0]
colunas = lista_aux[1]

# Construção de matriz em uma lista só
# As linhas são listas dentro de listas
for b in range(linhas):
    lista_principal.append([])

# As colunas são strings vazias dentro da lista que representa a respectiva linha
for c in lista_principal:
    for d in range(colunas):
        c.append(' ')

# Recebe a quantidade de itens que Eliza levou para o concurso
qtd_elementos = int(input())


for i in range(qtd_elementos):
    # Recebe o nível de atratividade do ítem + a sua posição na matriz no formato 'nivel_atratividade (i,j)'
    entrada = input()
    # Separa o elemento da sua localização por meio de split
    elemento, local = entrada.split(' ', 1)
    # Variável de apoio
    loc_def = ''
    # Retirada de parênteses da localização para ajudar na construção da lógica
    for d in local:
        if d == '(' or d == ')':
            loc_def += ''
        else:
            loc_def += d
    # Transforma a nova string sem parênteses numa lista
    local = loc_def.split(',')

    # Transforma cada elemento dessa lista de localização em int
    for e in range(len(local)):
        local[e] = int(local[e])

    # Coloca o elemento no seu lugar correto na matriz principal, de acordo com as coordenadas/localização dada pelo usuário
    lista_principal[local[0]][local[1]] = elemento

# Troca os espaços vazios por zeros
for f in range(len(lista_principal)):
    for g in range (len(lista_principal[f])):
        if lista_principal[f][g] == ' ':
            lista_principal[f][g] = '0'

# Variável que mantém o loop ativo
calculo = True

while calculo:
    # Recebe as operações 
    comando = input()
    # Construção de lógica para a operação de permutação (troca elementos de lugar)
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
    
    # Construção de lógica para a operação de transposição (troca as linhas pelas colunas e vice-versa)
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
    
    # Construção de lógica para a operação de remoção (remove o menor elemento da matriz e substitui por zero)
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
    
    # Se o comando for qualquer outro, o loop termina
    else:
        calculo = False

# Output exigido pelo desafio
print('Atual Arranjo:')
for r in range(len(lista_principal)):
    print(' '.join(lista_principal[r]))
