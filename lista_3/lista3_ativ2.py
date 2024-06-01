# Atividade 2 da Lista 3

investigacao = True
lista = []

# Variáveis com textos para evitar erros nas sintaxes das condições
altissima = 'Novo suspeito - altíssima periculosidade'
pouco = 'Novo suspeito - pouco perigoso'
livre = 'Livre de suspeita, pode remover'
perigoso = 'Sujeito mais perigoso do que pensávamos'
estranho = 'Que estranho, esses dois meliantes… troque-os de lugar'
nao_posicao = 'Essa posição não esta de acordo, ele não e tão perigoso assim'
como = 'Como a lista esta ficando?'
finalizar = 'Já temos nossa lista de suspeitos'


while investigacao:
    entrada = input()
    if entrada == altissima:
        nome = input()
        lista.insert(0, nome)
    elif entrada == pouco:
        nome = input()
        lista.append(nome)
    elif entrada == livre:
        nome = input()
        if nome in lista:
            lista.remove(nome)
    elif entrada == perigoso:
        indice_atual = int(input())
        indice_novo = int(input())
        # if 0 <= indice_atual < len(lista) and 0 <= indice_novo < len(lista):
        #     auxiliar_2 = lista.pop(indice_atual)
        #     lista.insert(indice_novo, auxiliar_2)
        if 0 <= indice_atual < len(lista) and 0 <= indice_novo < len(lista):
            lista[indice_atual], lista[indice_novo] = lista[indice_novo], lista[indice_atual]
    elif entrada == estranho:
        nome1 = input().strip()
        nome2 = input().strip()
        if nome1 in lista and nome2 in lista:
            indice1 = lista.index(nome1)
            indice2 = lista.index(nome2)
            lista[indice1], lista[indice2] = lista[indice2], lista[indice1]
        # nome = input()
        # b = lista.index(nome)
        # nome2 = input()
        # c = lista.index(nome2)
        # auxiliar = lista[b]
        # lista[b] = lista[c]
        # lista[c] = auxiliar
    elif entrada == nao_posicao:
        nome = input()
        if nome in lista:
            lista.append(nome)
            lista.remove(nome)
    elif entrada == como:
        print(', '.join(lista))
    elif entrada == finalizar:
        investigacao = False
        print('O resultado final ficou assim:')
        print(', '.join(lista))