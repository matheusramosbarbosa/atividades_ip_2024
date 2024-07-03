# Atividade 6 da Lista 4

def dividir_lista(lista, tamanho):
    sublistas = []
    for i in range(0, len(lista), tamanho):
        sublistas.append(lista[i:i + tamanho])
    return sublistas

def arredondar_de_30_em_30(n):
    if n % 30 == 0:
        return n
    else:
        return ((n // 30) + 1) * 30

def adicionar_pokemon(lista, quantidade):
    contador = 0
    i = 0
    # Adiciona pokémons na lista existente
    while i < len(lista) and contador < quantidade:
        if lista[i] == '0':
            lista[i] = '1'
            contador += 1
        i += 1
    # Adiciona pokémons e zeros para completar o box
    while contador < quantidade:
        lista.append('1')
        contador += 1
    while len(lista) % 30 != 0:
        lista.append('0')
    return lista

def remover_pokemon(lista, quantidade):
    contador = 0
    i = len(lista) - 1
    while i >= 0 and contador < quantidade:
        if lista[i] == '1':
            lista[i] = '0'
            contador += 1
        i -= 1
    
    # Remover boxes vazias sem usar break ou continue
    remover_zeros = True
    while len(lista) > 30 and remover_zeros:
        box_vazio = True
        j = len(lista) - 30
        while j < len(lista) and box_vazio:
            if lista[j] != '0':
                box_vazio = False
                remover_zeros = False  # Altera a variável de controle para sair do loop externo
            j += 1
        if box_vazio:
            lista = lista[:-30]
        else:
            remover_zeros = False
    
    return lista

def print_de_matrizes(a):
    linhas = 5
    colunas = 6
    b = dividir_lista(a, 30)
    c = [dividir_lista(sublista, colunas) for sublista in b]
    for j in range(len(c)):
        print(f'BOX {j + 1}:')
        for i in range(min(linhas, len(c[j]))):
            print(" ".join(c[j][i]))
        print()

matriz_inicial = ['0'] * 30

pokemons_armazenados = int(input())
arredondado = arredondar_de_30_em_30(pokemons_armazenados)

for i in range(arredondado - 30):
    matriz_inicial.append('0')

for i in range(pokemons_armazenados):
    matriz_inicial[i] = '1'

nova_lista = matriz_inicial.copy()

programa = True
while programa:
    comando = input()
    if comando == "Capturar":
        qtd = int(input())
        nova_lista = adicionar_pokemon(nova_lista, qtd)
        print_de_matrizes(nova_lista)
    elif comando == "Transferir":
        qtd = int(input())
        nova_lista = remover_pokemon(nova_lista, qtd)
        print_de_matrizes(nova_lista)
    elif comando == "Finalizar":
        programa = False

qtd_pokemon = nova_lista.count('1')

nova_lista = dividir_lista(nova_lista, 30)
sublistas_finais = [dividir_lista(sublista, 5) for sublista in nova_lista]

print('RELATÓRIO FINAL:\n')
print(f'BOXES: {len(sublistas_finais)}')
print(f'POKEMONS: {qtd_pokemon}')
