# # Atividade 7 da Lista 3

# tam_lista = input()
# lista_aux = tam_lista.split(' x ')
# for a in range(len(lista_aux)):
#     lista_aux[a] = int(lista_aux[a])

# lista_principal = []

# linhas = lista_aux[0]
# colunas = lista_aux[1]

# for b in range(linhas):
#     lista_principal.append([])

# for c in lista_principal:
#     for d in range(colunas):
#         c.append('')

# print(lista_principal)
    

# print(lista_aux)

# qtd_elementos = int(input())
# loc_def = ''

# entrada = input()
# elemento, local = entrada.split(' ', 1)
# print(elemento)
# print(local)
# for d in local:
#     if d == '(' or d == ')':
#         loc_def += ''
#     else:
#         loc_def += d
# local = loc_def.split(',')
# print(local)

# for e in range(len(local)):
#     local[e] = int(local[e])
# print(local)

# lista_principal[local[0]][local[1]] = elemento
# print(lista_principal)

# transposicao de matriz

colunas = 2
linhas = 3

lista = [['8', '9'], ['0', '6'], ['7', '0']]
nova_lista = []

linhas, colunas = colunas, linhas

print(linhas)
print(colunas)

for a in range(linhas):
    nova_lista.append([])

for c in nova_lista:
    for d in range(colunas):
        c.append('')

print(nova_lista)

for e in range(len(nova_lista)):
    for f in range(len(nova_lista[e])):
        nova_lista[e][f] = lista[f][e]

print(nova_lista)