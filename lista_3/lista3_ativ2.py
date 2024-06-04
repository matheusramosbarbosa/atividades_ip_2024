# Atividade 2 da Lista 3

# Variáveis de apoio para a questão
investigacao = True
lista = [] # Lista de suspeitos

# Variáveis com textos para evitar erros nas sintaxes das condições
altissima = 'Novo suspeito - altíssima periculosidade'
pouco = 'Novo suspeito - pouco perigoso'
livre = 'Livre de suspeita, pode remover'
perigoso = 'Sujeito mais perigoso do que pensávamos'
estranho = 'Que estranho, esses dois meliantes… troque-os de lugar'
nao_posicao = 'Essa posição não esta de acordo, ele não e tão perigoso assim'
como = 'Como a lista esta ficando?'
finalizar = 'Já temos nossa lista de suspeitos'

# Loop para definir se a investigação está ativa
while investigacao:
    # Input exigido pelo desafio
    entrada = input()
    # Condições para definir o que deverá ser feito de acordo com o comando
    # Algumas condições recebem o nome do suspeito em questão, e outras servem para trocar de lugar suspeito x com suspeito y, por exemplo
    # Nessa condição, caso o suspeito seja de altissima periculosidade, é usado insert(primeira_pos da lista, nome do suspeito)
    if entrada == altissima:
        nome = input()
        lista.insert(0, nome)
    # Nessa condição, caso o suspeito seja pouco perigoso, então ele é jogado para o final da lista de suspeitos
    elif entrada == pouco:
        nome = input()
        lista.append(nome)
    # Nessa condição, caso o suspeito não seja suspeito, ele é removido da lista
    elif entrada == livre:
        nome = input()
        if nome in lista:
            lista.remove(nome)
    # Se o suspeito for mais perigoso do que o esperado, ele deverá sair de uma posição (índice x, da posição antiga) e ir pra outra (índice y, da posição nova). Foi utilizado índices no intervalo de 0 a N - 1, então foi mais fácil de desenvolver
    elif entrada == perigoso:
        indice_atual = int(input())
        indice_novo = int(input())
        # Comparando se o índice dado pelo usuário realmente existe no tamanho da lista
        if 0 <= indice_atual < len(lista) and 0 <= indice_novo < len(lista):
            lista[indice_atual], lista[indice_novo] = lista[indice_novo], lista[indice_atual]
    # Se dois suspeitos forem estranhos, deverá trocar um de lugar com o outro
    elif entrada == estranho:
        nome1 = input()
        nome2 = input()
        # Condição para ver se os nomes da entrada realmente existem na lista
        if nome1 in lista and nome2 in lista:
            indice1 = lista.index(nome1) # Pegando o índice desse nome na lista principal
            indice2 = lista.index(nome2) # Pegando o índice desse nome na lista principal
            lista[indice1], lista[indice2] = lista[indice2], lista[indice1] # Troca de lugar dos elementos na lista
    # Se algum suspeito não for tão perigoso, ele será jogado para o final da lista
    elif entrada == nao_posicao:
        nome = input()
        if nome in lista:
            # Joga o nome para o final da lista
            lista.append(nome)
            # Remove a primeira ocorrência desse mesmo nome, pois ele ainda não havia sido removido da lista
            lista.remove(nome)
    # Nessa condição, retorna o estado atual da lista, separando cada nome por vírgula e espaço (, )
    elif entrada == como:
        print(', '.join(lista))
    # Caso o usuário deseje finalizar a investigação, a variável do while se torna falsa, e finaliza o loop
    elif entrada == finalizar:
        investigacao = False
        # Output final exigido pelo desafio
        print('O resultado final ficou assim:')
        print(', '.join(lista))