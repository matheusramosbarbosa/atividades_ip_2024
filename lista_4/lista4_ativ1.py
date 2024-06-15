# Atividade 1 da Lista 4

# Pode usar: funções básicas, listas, condicionais e loops

# CP Máximo = (ataque * (defesa**0.5)) * (stamina**0.5) * (CP Multiplicador**2)) / 10

def cp_maximo(a, b, c, d):
    cp_max = (a * (b**0.5) * (c**0.5) * (d**2)) / 10
    return cp_max

def desempate(a, b):
    if len(a) > len(b):
        c = a
    else:
        c = b
    return c


analise = True
lista_nome = []
lista_ataque = []
lista_defesa = []
lista_stamina = []
lista_multiplicador = []
lista_maiores_poke = []
valor_maior_poke = 0
empate = 0

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

for i in range(len(lista_nome)):
    cp_max = cp_maximo(lista_ataque[i], lista_defesa[i], lista_stamina[i], lista_multiplicador[i])
    # if cp_max == valor_maior_poke:
    #     if len(maior_poke) > len(lista_nome[i]):
    #         maior_poke = maior_poke
    #     else:
    #         maior_poke = lista_nome[i]
    if cp_max > valor_maior_poke:
        valor_maior_poke = cp_max
        maior_poke = lista_nome[i]

for i in range(len(lista_nome)):
    cp_max = cp_maximo(lista_ataque[i], lista_defesa[i], lista_stamina[i], lista_multiplicador[i])
    if valor_maior_poke == cp_max:
        lista_maiores_poke.append(lista_nome[i])

if len(lista_maiores_poke) > 1:
    for i in range(len(lista_maiores_poke)):
        pokemon_final = desempate(maior_poke, lista_nome[i])

if len(lista_maiores_poke) < 2:
    print(f'O Pokémon com o maior CP na região de Kanto é: {maior_poke}, com CP máximo de {valor_maior_poke:.2f}')
else:
    print(f'Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {pokemon_final}, com CP máximo de {valor_maior_poke:.2f}')