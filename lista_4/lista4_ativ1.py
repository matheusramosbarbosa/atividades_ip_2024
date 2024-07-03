# Atividade 1 da Lista 4

# Função para calcular o CP máximo de um Pokémon
def cp_maximo(a, b, c, d):
    # Calcula o CP máximo usando a fórmula dada
    cp_max = (a * (b**0.5) * (c**0.5) * (d**2)) / 10
    return cp_max

# Função para desempatar
def desempate(a, b):
    if len(a) > len(b):
        c = a
    else:
        c = b
    return c

# Variável para continuar a análise
analise = True
# Listas para armazenar informações dos Pokémon
lista_nome = []
lista_ataque = []
lista_defesa = []
lista_stamina = []
lista_multiplicador = []
# Lista e variável para armazenar o Pokémon com maior CP
lista_maiores_poke = []
valor_maior_poke = 0

# Loop para continuar a análise enquanto o usuário quiser
while analise:
    nome_pokemon = input()
    if nome_pokemon == "Fim":
        analise = False
    elif nome_pokemon not in lista_nome:
        lista_nome.append(nome_pokemon)
        qt_ataque = int(input())
        qt_defesa = int(input())
        qt_stamina = int(input())
        cp_multiplicador = float(input())
        lista_ataque.append(qt_ataque)
        lista_defesa.append(qt_defesa)
        lista_stamina.append(qt_stamina)
        lista_multiplicador.append(cp_multiplicador)
        print(f'Pokémon computado com sucesso.')
    else:
        print(f'Opa, esse Pokémon já foi analisado.')

# Verifica o CP máximo de cada Pokémon e guarda o maior CP
for i in range(len(lista_nome)):
    cp_max = cp_maximo(lista_ataque[i], lista_defesa[i], lista_stamina[i], lista_multiplicador[i])
    if cp_max > valor_maior_poke:
        valor_maior_poke = cp_max
        maior_poke = lista_nome[i]

# Adiciona todos os Pokémon com o maior CP na lista de desempate
for i in range(len(lista_nome)):
    cp_max = cp_maximo(lista_ataque[i], lista_defesa[i], lista_stamina[i], lista_multiplicador[i])
    if valor_maior_poke == cp_max:
        lista_maiores_poke.append(lista_nome[i])

# Se tiver mais de um Pokémon com o maior CP, desempata
if len(lista_maiores_poke) > 1:
    for i in range(len(lista_maiores_poke)):
        pokemon_final = desempate(maior_poke, lista_nome[i])

# Output exigido pelo desafio
if len(lista_maiores_poke) < 2:
    print(f'O Pokémon com o maior CP na região de Kanto é: {maior_poke}, com CP máximo de {valor_maior_poke:.2f}')
else:
    print(f'Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {pokemon_final}, com CP máximo de {valor_maior_poke:.2f}')
