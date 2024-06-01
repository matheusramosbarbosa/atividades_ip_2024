# Atividade 4 da Lista 3

# Ordem: Agricultura, Criação de animais, Pesca e Mineração

agricultura = input()
lista_agro = agricultura.split(' - ')
criacao = input()
lista_criacao = criacao.split(' - ')
pesca = input()
lista_pesca = pesca.split(' - ')
mineracao = input()
lista_mine = mineracao.split(' - ')

combinacao = []

print("Itens selecionados! Hora de iniciar a mesclagem... Simbora!")

#
gostou = True
sim = 'Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...'
nao = 'Esses itens são bem paia, acho que não gostei muito :('
de_novo = 'Bom, vamos tentar mais uma vez...'
encerrar = 'Essa máquina deve estar com defeito...'

while gostou:
    idx_agro = int(input())
    idx_criacao = int(input())
    idx_pesca = int(input())
    idx_mine = int(input())
    print("Combinando Itens...")
    combinacao.append(lista_agro[idx_agro])
    combinacao.append(lista_criacao[idx_criacao])
    combinacao.append(lista_pesca[idx_pesca])
    combinacao.append(lista_mine[idx_mine])
    print(f'Item para agricultura: {combinacao[0]}\nItem para criação: {combinacao[1]}\nItem para pesca: {combinacao[2]}\nItem para mineração: {combinacao[3]}')

    se_gostou = input()

    if se_gostou == sim:
        gostou = False
        print('Meu dia tá garantido, obrigado pela ajuda Pega Móvel!')
    elif se_gostou == nao:
        comando = input()
        if comando ==  de_novo:
            combinacao = []
            se_gostou = ''
        elif comando == encerrar:
            gostou = False
            print('É... acho que já chega de Stardew por hoje...')


