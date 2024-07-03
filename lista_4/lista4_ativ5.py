# Atividade 5 da Lista 4

def conversao_valores(b, a=[]):
    a = b.split(", ")
    a[2] = int(a[2])
    a[3] = int(a[3])
    a[4] = int(a[4])
    a[5] = int(a[5])
    a[6] = int(a[6])
    a[8] = int(a[8])
    c = a
    return c

def atacar(nivel, poder, defesa_inimigo, poder_ataque, efetividade):
    dano = ((((2* nivel) + 10) / 250) * (poder/defesa_inimigo * poder_ataque) + 2) * (efetividade)
    return dano

def org_efetividade(a):
    if a == "fogo":
        # lista = fraco contra | forte contra | neutro contra
        lista = [['agua'], ['grama'], ['fogo', 'normal']]
    elif a == "agua":
        lista = [['grama'], ['fogo'], ['agua', 'normal']]
    elif a == 'grama':
        lista = [['fogo'], ['agua'], ['grama', 'normal']]
    elif a == 'normal':
        lista = [[], [], ['fogo', 'agua', 'grama', 'normal']]
    return lista

lista_efetividade = [0.5, 2, 1]


pokemon_info = input()
lista_info = conversao_valores(pokemon_info)
nome_pokemon = lista_info[0]
vida_total = lista_info[3]
vida_poke = vida_total

print(f'escolho você {nome_pokemon}')
se_combate = True
while se_combate:
    combate = input()
    if combate == 'um pokemon selvagem aparece!':
        print(f'vamo botar pra quebrar!')
        selvagem_info = input()
        lista_selvagem = conversao_valores(selvagem_info)
        if lista_selvagem[6] > lista_info[6]:
            primeiro = lista_selvagem[0]
            segundo = lista_info[0]
        else:
            primeiro = lista_info[0]
            segundo = lista_selvagem[0]
        lista_inimigo = lista_selvagem
        inimigo = lista_selvagem[0]
        vida_total_inimigo = lista_inimigo[3]
    elif combate == 'Equipe Rocket':
        print(f'{nome_pokemon}, bora acabar com a raça desses bandidos e salvar o professor!')
        rocket_info = input()
        lista_rocket = conversao_valores(rocket_info)
        if lista_rocket[6] > lista_info[6]:
            primeiro = lista_rocket[0]
            segundo = lista_info[0]
        else:
            primeiro = lista_info[0]
            segundo = lista_rocket[0]
        lista_inimigo = lista_rocket
        inimigo = lista_rocket[0]
        vida_total_inimigo = lista_inimigo[3]

    efetividade_pokemon = org_efetividade(lista_info[1])
    efetividade_inimigo = org_efetividade(lista_inimigo[1])

    for i in efetividade_pokemon:
        if lista_inimigo[1] in i:
            aux = efetividade_pokemon.index(i)
            valor_ef_pokemon = lista_efetividade[aux]
    for i in efetividade_inimigo:
        if lista_info[1] in i:
            aux = efetividade_inimigo.index(i)
            valor_ef_inimigo = lista_efetividade[aux]

    vida_inimigo = lista_inimigo[3]

    if vida_poke == lista_info[3]:
        vida_poke = lista_info[3]


    print()

    luta = True

    while luta:
        if vida_inimigo > 0 and vida_poke > 0:
            comando = input()
            if comando == "correr":
                if combate == "Equipe Rocket":
                    print(f"lascou, eles não largam do meu pé!")
                else:
                    print(f'ufa, consegui meter o pé!')
                    luta = False
            else:
                if primeiro == nome_pokemon:
                    if comando == "atacar":
                        ataque = atacar(lista_info[2], lista_info[4], lista_inimigo[5], lista_info[8], valor_ef_pokemon)
                        ataque = int(ataque)
                        vida_inimigo -= ataque
                        print(f"{nome_pokemon} usou {lista_info[7]}")
                        if valor_ef_pokemon == 2:
                            print(f'foi super efetivo!')
                        elif valor_ef_pokemon == 0.5:
                            print(f'não foi muito efetivo')
                elif primeiro == inimigo:
                    ataque = atacar(lista_inimigo[2], lista_inimigo[4], lista_info[5], lista_inimigo[8], valor_ef_inimigo)
                    ataque = int(ataque)
                    vida_poke -= ataque
                    print(f"{inimigo} usou {lista_inimigo[7]}")
                    if valor_ef_inimigo == 2:
                        print(f'foi super efetivo!')
                    elif valor_ef_inimigo == 0.5:
                        print(f'não foi muito efetivo')
                if vida_inimigo > 0 and vida_poke > 0:
                    if segundo == nome_pokemon:
                        if comando == "atacar":
                            ataque = atacar(lista_info[2], lista_info[4], lista_inimigo[5], lista_info[8], valor_ef_pokemon)
                            ataque = int(ataque)
                            vida_inimigo -= ataque
                            print(f"{nome_pokemon} usou {lista_info[7]}")
                            if valor_ef_pokemon == 2:
                                print(f'foi super efetivo!')
                            elif valor_ef_pokemon == 0.5:
                                print(f'não foi muito efetivo')
                    elif segundo == inimigo:
                        ataque = atacar(lista_inimigo[2], lista_inimigo[4], lista_info[5], lista_inimigo[8], valor_ef_inimigo)
                        ataque = int(ataque)
                        vida_poke -= ataque
                        print(f"{inimigo} usou {lista_inimigo[7]}")
                        if valor_ef_inimigo == 2:
                            print(f'foi super efetivo!')
                        elif valor_ef_inimigo == 0.5:
                            print(f'não foi muito efetivo')
                if vida_poke > 0 and vida_inimigo > 0:
                    print(f'HP: {vida_poke}/{vida_total} | HP inimigo: {vida_inimigo}/{vida_total_inimigo}')
                elif vida_poke <= 0:
                    vida_poke = 0
                    print(f'HP: {vida_poke}/{vida_total} | HP inimigo: {vida_inimigo}/{vida_total_inimigo}')
                    vida_inimigo = 0
                    print(f'{nome_pokemon} derrotado!')
                    print()
                    se_combate = False
                    luta = False
                    print(f'Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
                elif vida_inimigo <= 0:
                    vida_inimigo = 0
                    print(f'HP: {vida_poke}/{vida_total} | HP inimigo: {vida_inimigo}/{vida_total_inimigo}')
                    luta = False
                    print(f'{inimigo} derrotado!')
                    print()
                    if combate == "Equipe Rocket":
                        print(f'Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {nome_pokemon}?')
                        se_combate = False