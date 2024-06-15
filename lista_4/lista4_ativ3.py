# Atividade 3 da Lista 4
nomes_tipos_aux = ["Misty", "Gary", "Ivy", "Blanche", "Ash", "Ritchie", "Surge", "Spark", "May", "Blaine", "Candela", "Agatha", "Sabrina", "Fantina", "Jessie", "James", "Giovanni", "Lorelei", "Dawn", "Max", "Erika", "Tracey", "Mallow", "Whitney"]
nomes_tipos = [["Misty", "Gary", "Ivy", "Blanche"], ["Ash", "Ritchie", "Surge", "Spark"], ["May", "Blaine", "Candela"], ["Agatha", "Sabrina", "Fantina"], ["Jessie", "James", "Giovanni"], ["Lorelei", "Dawn"], ["Max", "Erika", "Tracey", "Mallow"], ["Whitney"]]
letras = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def tipo_evie_lower(nome_lower, idade):
    somatorio = 0
    index_aux = 0
    for i in nome_lower:
        index_aux = letras.index(i)
        somatorio += index_aux
    passo_2 = somatorio * idade
    passo_3 = passo_2 % 8
    return passo_3

def tipo_evie_nome(nome_capitalize):
    for i in nomes_tipos:
        if nome_capitalize in i:
            tipo = i
    aux_index = nomes_tipos.index(tipo)
    return aux_index

def processamento_info(info, nomes, idades, nome='', idade=0):
    nome, idade = info.split(" - ")
    # idade = (int(idade))
    names = nomes.append(nome)
    ages = idades.append(int(idade))
    return names, ages


n = int(input())
lista_nomes = []
lista_idades = []

for i in range(n):
    informacoes = input()
    processamento = processamento_info(informacoes, lista_nomes, lista_idades)

lista_lower = []
for i in range(len(lista_nomes)):
    lista_lower.append(lista_nomes[i].lower())

lista_capitalize = []
for i in range(len(lista_nomes)):
    lista_capitalize.append(lista_lower[i].capitalize())

lista_indices = []

for i in range(len(lista_nomes)):
    if lista_capitalize[i] in nomes_tipos_aux:
        tipo_do_evie = tipo_evie_nome(lista_capitalize[i])
        lista_indices.append(tipo_do_evie)
    elif lista_lower[i] not in nomes_tipos_aux:
        tipo_do_evie = tipo_evie_lower(lista_lower[i], lista_idades[i])
        lista_indices.append(tipo_do_evie)

for i in range(len(lista_indices)):
    if lista_indices[i] == 0:
        print(f"A evolução do Eevee de {lista_capitalize[i]} é para Vaporeon, o mestre das águas!")
    elif lista_indices[i] == 1:
        print(f"O Eevee de {lista_capitalize[i]} evoluiu para Jolteon, cheio de energia elétrica!")
    elif lista_indices[i] == 2:
        print(f"O Eevee de {lista_capitalize[i]} se transformou em Flareon, dominando o calor do fogo!")
    elif lista_indices[i] == 3:
        print(f"Espeon é a evolução do Eevee de {lista_capitalize[i]}, mostrando sua mente brilhante!")
    elif lista_indices[i] == 4:
        print(f"A evolução sombria do Eevee de {lista_capitalize[i]} é Umbreon, deslizando pelas sombras!")
    elif lista_indices[i] == 5:
        print(f"Glaceon é o novo estágio do Eevee de {lista_capitalize[i]}, tão frio quanto o gelo!")
    elif lista_indices[i] == 6:
        print(f"O Eevee de {lista_capitalize[i]} se transformou em Leafeon, um espírito da floresta!")
    elif lista_indices[i] == 7:
        print(f"Sylveon é a evolução mágica do Eevee de {lista_capitalize[i]}, irradiando bondade e misticismo!")