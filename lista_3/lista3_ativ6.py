# Atividade 6 da Lista 3

# Tarefas de anjolina

# Input exigido pelo desafio
qtd_galinheiros = int(input())
# Lista de possíveis espécies
possiveis_especies = ['Coelho', 'Galinha', 'Pato']
lista_final = [] # Lista de apoio

# Variáveis de apoio
qtd_coelhos = 0
qtd_galinhas = 0
qtd_patos = 0

# For de acordo com a quantidade de galinheiros
for i in range (qtd_galinheiros):
    # Recebe as espécies separadas por vírgula
    especies = input()
    lista_especies = especies.split(', ')
    lista_final = lista_final + lista_especies # Adiciona na lista principal

# Para cada espécie possível, adiciona 1 ao contador da respectiva espécie.
for i in lista_final:
    if i == 'Coelho':
        qtd_coelhos += 1
    elif i == 'Galinha':
        qtd_galinhas += 1
    elif i == 'Pato':
        qtd_patos += 1

# Condições para definir os outputs exigidos pelo desafio
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


# Tarefas de Ricardo

# Inputs exigidos pelo desafio
compras = input()
lista_compras = compras.split(', ') # Transforma em lista

# Condição para definir print de output exigido pelo desafio
if 'Melão' in lista_compras:
    print(f'Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...')

sementes = input()
lista_sementes = sementes.split(', ') # Transforma em lista

# Listas de apoio que receberão informações
comprou = [] # Quais itens comprou
falta = [] # Quais itens faltam

# Para cada elemento da lista de compras, é verificado se está na lista de sementes vendidas pelo pierre, adicionado a uma lista de itens que foram comprados
for a in lista_compras:
    if a in lista_sementes:
        comprou.append(a)

# Caso não tenha conseguido comprar tudo, adiciona numa lista de itens que faltam
for a in lista_compras:
    if a not in comprou:
        falta.append(a)

# Condição para definir outputs exigidos pelo desafio
if not falta:
    print(f'Consegui comprar todas as frutas que queria!')
elif falta and (len(falta) == len(lista_compras)):
    print(f'Poxa, acho que ficaremos sem plantações.')
elif falta and (len(falta) < len(lista_compras)):
    print(f'Consegui comprar as seguintes sementes:')
    ordem_crescente = sorted(comprou)
    ordem_crescente = ', '.join(ordem_crescente)
    print(ordem_crescente)


# Tarefas de Stefan

# Input exigidos pelo desafio
materiais = input()
lista_materiais = materiais.split(', ') # Transforma em lista
qtd_itens = input()
lista_qtd_itens = qtd_itens.split(', ') # Transforma em lista

# Transforma string em int
for c in range(len(lista_qtd_itens)):
    lista_qtd_itens[c] = int(lista_qtd_itens[c]) 

# Variável para manter loop em funcionamento
crafting = True

# Variável de apoio
qtd_pararaios = 0

# Condição para adicionar os materiais realmente necessários numa lista a parte
if "Barra de ferro" in lista_materiais:
    index_ferro = lista_materiais.index('Barra de ferro')
    qtd_ferro = lista_qtd_itens[index_ferro]
if "Quartzo refinado" in lista_materiais:
    index_quartzo = lista_materiais.index('Quartzo refinado')
    qtd_quartzo = lista_qtd_itens[index_quartzo]
if "Asa de morcego" in lista_materiais:
    index_asa = lista_materiais.index('Asa de morcego')
    qtd_asa = lista_qtd_itens[index_asa]

# Loop para a criação do para-raios
while crafting:
    if qtd_ferro >= 1 and qtd_quartzo >= 1 and qtd_asa >= 5:
        qtd_pararaios += 1
        qtd_ferro -= 1
        qtd_quartzo -= 1
        qtd_asa -= 5
    # Caso acabe os itens suficientes para criar o para-raios, então cancela o loop
    else:
        crafting = False

# Output exigido pelo desafio
print(f'Com os itens que tenho, consigo fazer {qtd_pararaios} para-raios!')