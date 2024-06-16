# Atividade 5 da Lista 4

def conversao_valores(a):
    a[2] = int(a[2])
    a[3] = int(a[3])
    a[4] = int(a[4])
    a[5] = int(a[5])
    a[6] = int(a[6])
    a[8] = int(a[8])

pokemon_info = input()
lista_info = pokemon_info.split(", ")
conversao_valores(lista_info)

print(lista_info)

combate = input()
if combate == 'um pokemon selvagem aparece!':
    selvagem_info = input()
    lista_selvagem = selvagem_info.split(", ")
    conversao_valores(lista_selvagem)
elif combate == 'Equipe Rocket!':
    rocket_info = input()
    lista_rocket = rocket_info.split(", ")
    conversao_valores(lista_rocket)
