# Atividade 5 da Lista 3

# Lista com todos os peixes do vale
lista = ["Anchova", "Atum", "Bagre", "Baiacu", "Cioba", "Enguia", "Esturjão", "Linguado", "Pepino-do-mar", "Polvo", "Salmão", "Sardinha", "Tilápia", "Truta", "Robalo"]

# principal = input()

for i in range(3):
    lista_do_pescador = []
    pescador = input()
    lista_do_pescador = pescador.split(': ')
    auxiliar = lista_do_pescador.pop(1)
    nova_lista = auxiliar.split(', ')
    lista_do_pescador = lista_do_pescador + nova_lista
    lista_de_peixes = []
    qtd_peixes = 0
    qtd_peixes_diferentes = 0
    qtd_mentiras = 0
    falta = []
    fim = False
    while not fim:
        peixe = input()
        if peixe == "FIM":
            fim = True
        else:
            if peixe not in lista_de_peixes:
                qtd_peixes_diferentes += 1
            lista_de_peixes.append(peixe)
            qtd_peixes += 1
    if "Pescador" in lista_do_pescador:
        if qtd_peixes_diferentes < 5:
            qtd_mentiras += 1
    if "Velho Marinheiro" in lista_do_pescador:
        if qtd_peixes_diferentes < 10:
            qtd_mentiras += 1
    if "Velho Pescador" in lista_do_pescador:
        for a in lista:
            if a not in lista_de_peixes:
                falta.append(a)
        if len(falta) > 0:
            qtd_mentiras += 1
    if "Deus Pescador" in lista_do_pescador:
        if len(lista_de_peixes) < 25:
            qtd_mentiras += 1
    if qtd_mentiras == 0:
        print(f'{lista_do_pescador[0]} realmente estava falando a verdade!!!')
    else:
        print(f'{lista_do_pescador[0]} é um mentiroso, ele não tem todas essas conquistas!')