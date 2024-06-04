# Atividade 4 da Lista 3

# Textos em variáveis para evitar erro nas sintaxes das condições
sim = 'Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...'
nao = 'Esses itens são bem paia, acho que não gostei muito :('
de_novo = 'Bom, vamos tentar mais uma vez...'
encerrar = 'Essa máquina deve estar com defeito...'

# Inputs exigidos pelo desafio, já transformando-os em listas, separando as strings por meio do split( - )
agricultura = input()
lista_agro = agricultura.split(' - ')
criacao = input()
lista_criacao = criacao.split(' - ')
pesca = input()
lista_pesca = pesca.split(' - ')
mineracao = input()
lista_mine = mineracao.split(' - ')

# Lista que irá receber os itens para a combinação
combinacao = []

# Output exigido pelo desafio
print("Itens selecionados! Hora de iniciar a mesclagem... Simbora!")

# Variável de apoio para manter o while em loop
gostou = True

while gostou:
    # Recebimento do índice de cada item no intervalo de 0 - N - 1
    idx_agro = int(input())
    idx_criacao = int(input())
    idx_pesca = int(input())
    idx_mine = int(input())

    # Output exigido pelo desafio
    print("Combinando Itens...")

    # Adicionando cada item na lista de combinação de acordo com os itens escolhidos acima, guiado por meio dos índices apontando para as posições em cada lista
    combinacao.append(lista_agro[idx_agro])
    combinacao.append(lista_criacao[idx_criacao])
    combinacao.append(lista_pesca[idx_pesca])
    combinacao.append(lista_mine[idx_mine])

    # Output exigido pelo desafio
    print(f'Item para agricultura: {combinacao[0]}\nItem para criação: {combinacao[1]}\nItem para pesca: {combinacao[2]}\nItem para mineração: {combinacao[3]}')

    # Input exigido pelo desafio (usuário diz se gostou da combinação)
    se_gostou = input()

    # Se ele gostou, então o loop termina
    if se_gostou == sim:
        gostou = False
        # Output exigido pelo desafio
        print('Meu dia tá garantido, obrigado pela ajuda Pega Móvel!')
    # Se ele não gostou, o usuário decide se vai continuar escolhendo os itens ou não
    elif se_gostou == nao:
        comando = input()
        if comando ==  de_novo:
            # Caso deseje tentar novamente, lista de itens e opinião são redefinidos
            combinacao = []
            se_gostou = ''
        # Caso deseje encerrar, o loop finaliza
        elif comando == encerrar:
            gostou = False
            # Output exigido pelo desafio
            print('É... acho que já chega de Stardew por hoje...')


