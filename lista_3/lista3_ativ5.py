# Atividade 5 da Lista 3

# Lista com todos os peixes do vale
lista = ["Anchova", "Atum", "Bagre", "Baiacu", "Cioba", "Enguia", "Esturjão", "Linguado", "Pepino-do-mar", "Polvo", "Salmão", "Sardinha", "Tilápia", "Truta", "Robalo"]

# For no intervalo da quantidade de pescadores
for i in range(3):
    # Lista que receberá as conquistas do pescador, redefinida a cada começo do for
    lista_do_pescador = []
    # Input exigido pelo desafio (recebe o nome do pescador e suas conquistas)
    pescador = input()
    # Separando a entrada do pescador em lista
    lista_do_pescador = pescador.split(': ')
    # Separando o segundo elemento da lista, que ainda não foi separado corretamente
    auxiliar = lista_do_pescador.pop(1)
    # Separando por meio da split e retornando à lista principal
    nova_lista = auxiliar.split(', ')
    lista_do_pescador = lista_do_pescador + nova_lista
    # Lista que receberá todos os peixes que o pescador pescou
    lista_de_peixes = []
    # Variáveis de apoio
    qtd_peixes = 0
    qtd_peixes_diferentes = 0
    qtd_mentiras = 0
    # Lista de apoio
    falta = []
    # Variável para manter o loop em repetição
    fim = False
    # Loop enquanto o usuário não terminar de escrever cada peixe
    while not fim:
        # Input que vai receber o peixe que o pescador pescou a cada começo de loop
        peixe = input()
        # Se receber "FIM", o loop termina
        if peixe == "FIM":
            fim = True
        else:
            # Põe a entrada (peixe) numa lista auxiliar para ajudar a juntar todos os peixes numa lsita só
            # Caso, ao rodar o loop, o peixe já esteja na lista, ele será adicionado novamente, mas será adicionado 1 ao contador de quantidade de peixes diferentes, necessário para definir se a conquista realmente ocorreu
            if peixe not in lista_de_peixes:
                qtd_peixes_diferentes += 1
            lista_de_peixes.append(peixe)
            # Contador de quantidade de peixes no total
            qtd_peixes += 1
    # Se o pescador disser que conquistou a respectiva conquista, será analisado se ele está mentindo de acordo com a condição da conquista
    # Um contador de mentiras também é utilizado para auxiliar no resultado final
    if "Pescador" in lista_do_pescador:
        if qtd_peixes_diferentes < 5:
            qtd_mentiras += 1
    if "Velho Marinheiro" in lista_do_pescador:
        if qtd_peixes_diferentes < 10:
            qtd_mentiras += 1
    if "Velho Pescador" in lista_do_pescador:
        # Para cada elemento da lista de todos os peixes, se o elemento não existir na lista de pescados do pescador, é adicionado numa lista de peixes faltantes para conseguir a conquista de Velho Pescador
        for a in lista:
            if a not in lista_de_peixes:
                falta.append(a)
        # Se faltar mais de um peixe, então ele mentiu
        if len(falta) > 0:
            qtd_mentiras += 1
    if "Deus Pescador" in lista_do_pescador:
        if len(lista_de_peixes) < 25:
            qtd_mentiras += 1
    # Condição final
    # Caso o pescador tenha falado a verdade, é printado um output exigido pelo desafio. Caso contrário, é printado outro output exigido pelo desafio.
    if qtd_mentiras == 0:
        print(f'{lista_do_pescador[0]} realmente estava falando a verdade!!!')
    else:
        print(f'{lista_do_pescador[0]} é um mentiroso, ele não tem todas essas conquistas!')