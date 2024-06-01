# Atividade 3 da Lista 3

itens_desejados = input()
lista_desejados = itens_desejados.split(', ')
qtd_desejados = len(lista_desejados)
itens_encontrados = input()
lista_encontrados = itens_encontrados.split(', ')
qtd_encontrados = len(lista_encontrados)
comparacao = []
falta = []

for i in lista_desejados:
    if i in lista_encontrados:
        comparacao.append(i)

if not comparacao:
    print(f'Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {qtd_desejados} itens aqui na fazenda.')
else:
    print(f'Estes são os itens que já tenho na fazenda:')
    for i in range(len(comparacao)):
        print(f'{i + 1}º item: {comparacao[i]}')
    for a in lista_desejados:
        if a not in comparacao:
            falta.append(a)
    if not falta:
        print(f'Perfeito, encontrei todos os {qtd_desejados} itens aqui na fazenda!')
    else:
        print(f'Vou precisar adquirir {len(falta)} itens antes do festival!')
    print(f'Estou pronto para o festival de Stardew Valley! Que comece a diversão!')