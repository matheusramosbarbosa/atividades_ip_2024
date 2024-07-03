# Atividade 4 da Lista 4

# Listas com o alfabeto e seus valores ASCII
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
valor_ascii = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
cifra_traduzida = []

# Função para analisar a apresentação dos jogadores
def analise_apresentacao(texto):
    texto = texto.replace("Olá, meu nome é ", "")
    texto = texto.replace(", meu pokémon preferido é ", " - ")
    texto = texto.replace(" e tenho ", " - ")
    texto = texto.replace(" pokébolas", "")
    a = texto
    return a

# Função para analisar a aparição de pokémon selvagem
def analise_selvagem(texto):
    texto = texto.replace("Um ", "")
    texto = texto.replace(" selvagem apareceu! Foram ", " - ")
    texto = texto.replace(" segundos e ", " - ")
    texto = texto.replace(" passos desde o último encontro de ", " - ")
    a = texto
    return a

# Função para converter uma letra em uma cifra
def conversao_cifra(a):
    cifra_traduzida = []
    for i in range(a, a + 26, 1):
        caractere = alfabeto[i % len(alfabeto)]
        cifra_traduzida.append(caractere)
    b = cifra_traduzida
    return b

# Função para descobrir o ID do jogador
def descobrir_id_jogador(a, b):
    for i in a:
        id_jogador = 0
        for j in i:
            index_aux = alfabeto.index(j)
            id_jogador += valor_ascii[index_aux]
        b.append(str(id_jogador))
    c = b
    return c

# Função para descobrir o ID do pokémon
def descobrir_id_pokemon(a, b):
    id_pokemon = 0
    for j in a:
        index_aux = alfabeto.index(j)
        id_pokemon += valor_ascii[index_aux]
    id_final = id_pokemon * b
    c = str(id_final)
    return c 

# Listas para armazenar dados dos jogadores
lista_nomes = []
lista_fav = []
lista_qtd = []

# Número de participantes
n_participantes = int(input())

# Processa as informações dos participantes
for i in range(n_participantes):
    apresentacao = input()
    frase = analise_apresentacao(apresentacao)
    nomes, favs, qtds = frase.split(" - ")
    lista_nomes.append(nomes)
    lista_fav.append(favs)
    lista_qtd.append(int(qtds))

# Lista para armazenar os pokémons capturados
lista_pokemon = []
for i in range(n_participantes):
    lista_pokemon.append([])

# Converte os nomes para minúsculas
nomes_lower = [nome.lower() for nome in lista_nomes]

# Codifica os nomes usando a cifra
lista_codificados = []
cifra_traduzida = conversao_cifra(3)
for a in nomes_lower:
    nome_codificado = ''
    for i in a:
        index_aux = alfabeto.index(i)
        nome_codificado += cifra_traduzida[index_aux]
    lista_codificados.append(nome_codificado)

# Descobre o ID dos jogadores
lista_aux = []
lista_id_jogador = descobrir_id_jogador(lista_codificados, lista_aux)

# Loop para processar aparições de pokémons selvagens
campeonato = True
while campeonato:
    aparicao = input()
    texto_aparicao = analise_selvagem(aparicao)
    lista_info = texto_aparicao.split(" - ")
    lista_info[1] = int(lista_info[1])
    lista_info[2] = int(lista_info[2])
    lista_info[0], lista_info[3] = lista_info[3], lista_info[0]
    cifra_traduzida = conversao_cifra(lista_info[2])
    poke_lower = lista_info[3].lower()
    nome_codificado = ''
    for i in poke_lower:
        index_aux = alfabeto.index(i)
        nome_codificado += cifra_traduzida[index_aux]
    index_aux_2 = lista_nomes.index(lista_info[0])
    jogador_atual = lista_nomes[index_aux_2]
    pokemon_atual = lista_info[3]
    id_pokemon = descobrir_id_pokemon(nome_codificado, lista_info[1])
    lista_aux_jogador = []
    lista_aux_pokemon = []

    for i in lista_id_jogador[index_aux_2]:
        lista_aux_jogador.append(i)
    
    for i in id_pokemon:
        lista_aux_pokemon.append(i)

    shiny = False

    # Verifica se é um shiny
    if lista_aux_jogador[-1] == lista_aux_pokemon[-1]:
        shiny = True

    fav = False

    # Verifica se é o pokémon favorito
    if lista_info[3] == lista_fav[index_aux_2]:
        fav = True

    shiny_fav = False

    # Verifica se é um shiny e favorito
    if shiny and fav:
        shiny_fav = True

    # Lida com diferentes casos de captura
    if shiny_fav and lista_qtd[index_aux_2] == 1:
        lista_qtd[index_aux_2] -= 1
        print(f'{jogador_atual}: Que sorte! Não apenas achei meu shiny favorito, como também o capturei em minha última pokébola!!!')
        lista_pokemon[index_aux_2].append(pokemon_atual)
        campeonato = False
    elif shiny_fav and lista_qtd[index_aux_2] >= 1:
        lista_qtd[index_aux_2] -= 1
        print(f'{jogador_atual}: Consegui capturar um {lista_fav[index_aux_2]} shiny!')
        lista_pokemon[index_aux_2].append(pokemon_atual)
        campeonato = False
    elif pokemon_atual in lista_pokemon[index_aux_2] and shiny and lista_qtd[index_aux_2] >= 1:
        print(f'{jogador_atual}: Achei um {pokemon_atual} shiny, mas não posso desperdiçar pokébolas em um shiny que já tenho...')
    elif shiny and not fav and lista_qtd[index_aux_2] >= 1:
        lista_qtd[index_aux_2] -= 1
        print(f'{jogador_atual}: Mais um shiny para a coleção, mas ainda não é um {lista_fav[index_aux_2]}')
        lista_pokemon[index_aux_2].append(pokemon_atual)
    elif fav and lista_qtd[index_aux_2] >= 1 and not shiny:
        lista_qtd[index_aux_2] -= 1
        print(f'{jogador_atual}: Uau, um {lista_fav[index_aux_2]}! Pena que não é um shiny...')
    elif shiny_fav and lista_qtd[index_aux_2] == 0:
        print(f'{jogador_atual}: Só pode ser brincadeira, um {lista_fav[index_aux_2]} shiny logo agora?!')
    elif shiny and not fav and lista_qtd[index_aux_2] == 0:
        print(f'{jogador_atual}: Péssimo momento, encontrei um {pokemon_atual} shiny, mas não tenho mais pokébolas!')
    elif fav and lista_qtd[index_aux_2] == 0:
        print(f'{jogador_atual}: Desculpa, meu querido {lista_fav[index_aux_2]}, mas não poderei lhe capturar hoje')
    elif not fav and not shiny and lista_qtd[index_aux_2] == 0:
        print(f'{jogador_atual}: Só um {pokemon_atual} normal? Bom, não é como se eu tivesse pokébolas para capturar algo raro mesmo...')
    elif not fav and not shiny and lista_qtd[index_aux_2] >= 1:
        print(f'{jogador_atual}: Ainda não é um {lista_fav[index_aux_2]} shiny, tenho que continuar procurando...')

# Output exigido pelo desafio
print(f'\n---Vamos verificar o que todos encontraram!---')
for i in range(len(lista_nomes)):
    if len(lista_pokemon[i]) >= 1:
        frase_aux = ", ".join(lista_pokemon[i])
        print(f'{lista_nomes[i]} capturou os seguintes shinies: {frase_aux}')
    else:
        print(f'Coitado, {lista_nomes[i]} não conseguiu capturar um único shiny hoje')
