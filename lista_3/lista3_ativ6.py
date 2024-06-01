# Atividade 6 da Lista 3


# Anjolina
qtd_galinheiros = int(input())
possiveis_especies = ['Coelho', 'Galinha', 'Pato']
lista_final = []
qtd_coelhos = 0
qtd_galinhas = 0
qtd_patos = 0

for i in range (qtd_galinheiros):
    especies = input()
    lista_especies = especies.split(', ')
    lista_final = lista_final + lista_especies

for i in lista_final:
    if i == 'Coelho':
        qtd_coelhos += 1
    elif i == 'Galinha':
        qtd_galinhas += 1
    elif i == 'Pato':
        qtd_patos += 1

if qtd_coelhos > 0:
    print(f'A fazenda tem {qtd_coelhos} coelhos!')
else:
    print(f'Poxa que pena, não temos coelhos.')

if qtd_galinhas > 0:
    print(f'A fazenda tem {qtd_galinhas} galinhas!')
else:
    print(f'Poxa que pena, não temos galinhas.')

if qtd_patos > 0:
    print(f'A fazenda tem {qtd_patos} patos!')
else:
    print(f'Poxa que pena, não temos patos.')


# Ricardo
compras = input()
lista_compras = compras.split(', ')
if 'Melão' in lista_compras:
    print(f'Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...')
sementes = input()
lista_sementes = sementes.split(', ')
comprou = []
falta = []

for a in lista_compras:
    if a in lista_sementes:
        comprou.append(a)

for a in lista_compras:
    if a not in comprou:
        falta.append(a)

if not falta:
    print(f'Consegui comprar todas as frutas que queria!')
elif falta and (len(falta) == len(lista_compras)):
    print(f'Poxa, acho que ficaremos sem plantações.')
elif falta and (len(falta) < len(lista_compras)):
    print(f'Consegui comprar as seguintes sementes:')
    ordem_crescente = sorted(comprou)
    ordem_crescente = ', '.join(ordem_crescente)
    print(ordem_crescente)

# Stefan
materiais = input()
lista_materiais = materiais.split(', ')
qtd_itens = input()
lista_qtd_itens = qtd_itens.split(', ')
for c in range(len(lista_qtd_itens)):
    lista_qtd_itens[c] = int(lista_qtd_itens[c]) 

crafting = True
qtd_pararaios = 0

if "Barra de ferro" in lista_materiais:
    index_ferro = lista_materiais.index('Barra de ferro')
    qtd_ferro = lista_qtd_itens[index_ferro]
if "Quartzo refinado" in lista_materiais:
    index_quartzo = lista_materiais.index('Quartzo refinado')
    qtd_quartzo = lista_qtd_itens[index_quartzo]
if "Asa de morcego" in lista_materiais:
    index_asa = lista_materiais.index('Asa de morcego')
    qtd_asa = lista_qtd_itens[index_asa]

while crafting:
    if qtd_ferro >= 1 and qtd_quartzo >= 1 and qtd_asa >= 5:
        qtd_pararaios += 1
        qtd_ferro -= 1
        qtd_quartzo -= 1
        qtd_asa -= 5
    else:
        crafting = False

print(f'Com os itens que tenho, consigo fazer {qtd_pararaios} para-raios!')