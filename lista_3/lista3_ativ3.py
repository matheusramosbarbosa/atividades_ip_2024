# Atividade 3 da Lista 3

# Inputs exigidos pelo desafio
# Entrada de lista de itens desejados
itens_desejados = input()
#Transformando a string numa lista por meio de split
lista_desejados = itens_desejados.split(', ')
# Tamanho da lista de itens desejados
qtd_desejados = len(lista_desejados)

# Entrada de lista de itens já encontrados
itens_encontrados = input()
# Transformando a string numa lista por meio de split
lista_encontrados = itens_encontrados.split(', ')
# Tamanho da lista de itens encontrados
qtd_encontrados = len(lista_encontrados)

# Variáveis de apoio
encontrados_ordem = [] # Lista de apoio para adicionar os itens encontrados na mesma ordem dos itens desejados
falta = [] # Lista de apoio para colocar os itens que estão em falta

# For definindo se o item desejado analisado no momento se encontra na lista de itens encontrados.
# Se sim, adiciona numa lista auxiliar os encontrados na mesma ordem que aparecem na lista de itens desejados
for i in lista_desejados:
    if i in lista_encontrados:
        encontrados_ordem.append(i)

# Se a lista auxiliar estiver vazia, significa que nenhum item encontrado está na lista de itens desejados, então retorna um print
if not encontrados_ordem:
    print(f'Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {qtd_desejados} itens aqui na fazenda.')
else:
    # Do contrário, os itens que o usuário já possui (itens encontrados) são listados na ordem
    print(f'Estes são os itens que já tenho na fazenda:')
    # Print de cada item na ordem correta, para visualização do usuário
    for i in range(len(encontrados_ordem)):
        print(f'{i + 1}º item: {encontrados_ordem[i]}')
    # For definindo se os itens desejados estão todos na lista dos encontrados. Para cada item não encontrado, adiciona numa lista auxiliar (itens em falta)
    for a in lista_desejados:
        if a not in encontrados_ordem:
            falta.append(a)
    # Se não existir itens em falta, printar output exigido pelo desafio
    if not falta:
        print(f'Perfeito, encontrei todos os {qtd_desejados} itens aqui na fazenda!')
    else:
        # Do contrário, printar output exigido pelo desafio
        print(f'Vou precisar adquirir {len(falta)} itens antes do festival!')
    # Print de output exigido pelo desafio
    print(f'Estou pronto para o festival de Stardew Valley! Que comece a diversão!')