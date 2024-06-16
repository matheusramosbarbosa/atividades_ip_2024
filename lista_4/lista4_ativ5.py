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

print(f'escolho você {nome_pokemon}')

combate = input()
if combate == 'um pokemon selvagem aparece!':
    print(f'vamo botar pra quebrar!')
    selvagem_info = input()
    lista_selvagem = conversao_valores(selvagem_info)
    if lista_selvagem[5] > lista_info[5]:
        primeiro_lista = lista_selvagem
        primeiro = lista_selvagem[0]
        segundo_lista =  lista_info
        segundo = lista_info[0]
        lista_inimigo = lista_selvagem
        inimigo = lista_selvagem[0]
    else:
        primeiro_lista = lista_info
        primeiro = lista_info[0]
        segundo_lista = lista_selvagem
        segundo = lista_selvagem[0]
        lista_inimigo = lista_selvagem
        inimigo = lista_selvagem[0]
elif combate == 'Equipe Rocket!':
    print(f'{nome_pokemon}, bora acabar com a raça desses bandidos e salvar o professor!')
    rocket_info = input()
    lista_rocket = conversao_valores(rocket_info)
    if lista_rocket[5] > lista_info[5]:
        primeiro_lista = lista_rocket
        primeiro = lista_rocket[0]
        segundo_lista = lista_info
        segundo = lista_info[0]
        lista_inimigo = lista_rocket
        inimigo = lista_rocket[0]
    else:
        primeiro_lista = lista_info
        primeiro = lista_info[0]
        segundo_lista = lista_rocket
        segundo = lista_rocket[0]
        lista_inimigo = lista_rocket
        inimigo = lista_rocket[0]


print(primeiro_lista)
print(segundo_lista)
efetividade_primeiro = org_efetividade(primeiro_lista[1])
efetividade_segundo = org_efetividade(segundo_lista[1])
print(efetividade_primeiro)
print(efetividade_segundo)
vida_total = lista_info[3]
vida_total_inimigo = lista_inimigo[3]

for i in efetividade_primeiro:
    if segundo_lista[1] in i:
        aux = efetividade_primeiro.index(i)
        valor_ef_primeiro = lista_efetividade[aux]
for i in efetividade_segundo:
    if primeiro_lista[1] in i:
        aux = efetividade_segundo.index(i)
        valor_ef_segundo = lista_efetividade[aux]

print(valor_ef_primeiro)
print(valor_ef_segundo)


iniciar_combate = True

while primeiro_lista[3] > 0 and segundo_lista[3] > 0:
    print()
    comando = input()
    if comando == "atacar" and primeiro_lista[3] > 0:
        ataque = atacar(primeiro_lista[2], primeiro_lista[4], segundo_lista[5], primeiro_lista[8], efetividade_primeiro)
        if primeiro == inimigo:
            lista_info[3] -= ataque
            segundo_lista[3] -= ataque
        else:
            lista_inimigo[3] -= ataque
            segundo_lista[3] -= ataque
        if efetividade_primeiro == 2:
            print(f'foi super efetivo!')
        elif efetividade_primeiro == 0.5:
            print(f'não foi muito efetivo')
        print(f'HP: {lista_info[3]}/{vida_total}.')
        print(f'HP inimigo: {lista_inimigo[3]}/{vida_total_inimigo}')
    elif comando == "correr" and primeiro == nome_pokemon and primeiro_lista[3] > 0:
        print()
    comando = input()
    if comando == "atacar" and segundo_lista[3] > 0:
        ataque = atacar(segundo_lista[2], segundo_lista[4], primeiro_lista[5], segundo_lista[8], efetividade_segundo)
        if segundo == inimigo:
            lista_info[3] -= ataque
            primeiro_lista[3] -= ataque
        else:
            lista_inimigo[3] -= ataque
            segundo_lista[3] -= ataque
        if efetividade_segundo == 2:
            print(f'foi super efetivo!')
        elif efetividade_segundo == 0.5:
            print(f'não foi muito efetivo')
        print(f'HP: {lista_info[3]}/{vida_total}.')
        print(f'HP inimigo: {lista_inimigo[3]}/{vida_total_inimigo}')