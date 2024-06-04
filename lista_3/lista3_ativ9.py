# Atividade 9 da Lista 3

# Lista com todos os locais da fazenda
locais_fazenda = ['Torre do Mago', 'Rancho da Marnie', 'Saloon', 'Armazém do Pierre', 'Casa do Prefeito', 'Peixaria', 'Museu', 'Ferreiro', 'Mercado Joja', 'Carpintaria', 'Minas', 'Centro Comunitário']
# Lista com as suas respectivas distâncias
distancias = [700, 260, 1200, 1100, 1500, 1900, 1870, 1700, 1800, 1500, 1850, 1300]
# Lista com seus respectivos horários de funcionamento
horario_str = [['6:00', '23:00'], ['9:00', '16:00'], ['12:00', '00:00'], ['09:00', '17:00'], ['08:30', '22:00'], ['09:00', '17:00'], ['08:00', '18:00'], ['09:00', '16:00'], ['09:00', '23:00'], ['09:00', '17:00'], ['00:00', '23:59'], ['00:00', '23:59']]
# Lista com seus respectivos horários de funcionamento em decimal
horario_func = [[6.0, 23.0], [9.0, 16.0], [12.0, 23.99], [9.0, 17.0], [8.5, 22.0], [9.0, 17.0], [9.0, 18.0], [9.0, 16.0], [9.0, 23.0], [9.0, 17.0], [0.0, 23.99], [0.0, 23.99]]

# Listas de apoio da primeira análisa
lista_final = []
nomes = []
horarios = []
locais = []

# Listas de apoio da segunda análise
ladroes = []
local_roubo = []

# Listas de apoio da terceira análise
local_fechado = []
ladroes_fechado = []
horario_fechado = []

# Para i no intervalo dos 6 suspeitos
for i in range (6):
    # Input exigido pelodo desafio
    info_suspeitos = input()

    # Configuração das listas para melhorar a construção da lógica
    lista_suspeito1 = info_suspeitos.split(' - ')
    nomes.append(lista_suspeito1[0])

    horario_aux = lista_suspeito1[1]
    horario_aux_lista = horario_aux.split(':')
    for a in range(len(horario_aux_lista)):
        horario_aux_lista[a] = float(horario_aux_lista[a])
    horario_def = horario_aux_lista[0] + (horario_aux_lista[1]/60)

    horarios.append(horario_def)
    locais.append(lista_suspeito1[2])

# Análise de existencia de locais da fazenda
for b in locais:
    if b not in locais_fazenda:
        aux = locais.index(b)
        ladroes.append(nomes[aux])
        local_roubo.append(locais[aux])

# Primeira análise exigida pelo desafio
if len(ladroes) == 1:
    # Output exigido pelo desafio
    print(f'Esse lugar {local_roubo[0]} nem existe! {ladroes[0]} foi quem roubou os melões!')
elif len(ladroes) > 1:
    # Configuração de lista para colocá-la em ordem crescente (alfabética ou numérica)
    nome_ord_alf = sorted(ladroes)
    local_ord_alf = sorted(local_roubo)
    nomes_aux = ', '.join(nome_ord_alf)
    local_aux = ', '.join(local_ord_alf)
    # Output exigido pelo desafio
    print(f'{local_aux} nem existem! {nomes_aux} roubaram os melões!')
# Segunda análise exigida pelo desafio
else:
    for c in locais:
        aux = locais.index(c)
        aux2 = locais_fazenda.index(c)
        if horarios[aux] < horario_func[aux2][0] or horarios[aux] > horario_func[aux2][1]:
            local_fechado.append(locais[aux])
            ladroes_fechado.append(nomes[aux])
            horario_fechado.append(horario_str[aux2][1])
    
    if len(local_fechado) == 1:
        # Output exigido pelo desafio
        print(f'{local_fechado[0]} nem estava aberto nessa hora, esse lugar foi fechado às {horario_fechado[0]}! {ladroes_fechado[0]} roubou os melões!')
    elif len(local_fechado) > 1:
        # Configuração de lista para colocá-la em ordem crescente (alfabética ou numérica)
        nome_ord_alf = sorted(ladroes_fechado)
        local_ord_alf = sorted(local_fechado)
        nomes_aux = ', '.join(nome_ord_alf)
        local_aux = ', '.join(local_ord_alf)
        # Output exigido pelo desafio
        print(f'{local_aux} nem estavam abertos nessa hora, esses lugares foram fechados beeem antes! {nomes_aux} se uniram e roubaram os melões!')
    # Terceira análise exigida pelo desafio
    else:
        menor = float('inf')
        menor_distancia = 0
        ladrao_distancia = []
        distancias_jogadores = []

        for c in locais:
            aux = locais.index(c)
            aux2 = locais_fazenda.index(c)
            distancias_jogadores.append(distancias[aux2])

        for c in locais:
            aux = locais.index(c)
            aux2 = locais_fazenda.index(c)
            if distancias[aux2] < menor:
                menor = distancias[aux2]

        for c in range(len(locais)):
            if distancias_jogadores[c] == menor:
                ladrao_distancia.append(nomes[c])   

        if len(ladrao_distancia) == 1:
            # Output exigido pelo desafio
            print(f'{ladrao_distancia[0]} estava a {menor} metros da plantação! Agora é nosso suspeito número um. Fiquem de olho!')
        elif len(ladrao_distancia) > 1:
            # Configuração de lista para colocá-la em ordem crescente (alfabética ou numérica)
            nome_ord_alf = sorted(ladrao_distancia)
            nomes_aux = ', '.join(nome_ord_alf)
            # Output exigido pelo desafio
            print(f'{nomes_aux} estavam a {menor} metros da plantação! Eles podiam estar cometendo o roubo juntos... Fiquem de olho!')