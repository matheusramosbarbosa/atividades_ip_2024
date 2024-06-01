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