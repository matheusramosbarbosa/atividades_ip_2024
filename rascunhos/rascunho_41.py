def captacao_info(lista_nome, lista_fav, lista_qtd, frase_1):
    corte = slice(16, 34554)
    nova_frase_1 = frase_1[corte]
    lista_aux = nova_frase_1.split(',')
    a = lista_nome.append(lista_aux[0])
    tam_nome = len(lista_aux[0])
    novo_corte = 26 + tam_nome
    corte = slice(novo_corte, 34554)
    nova_frase_2 = nova_frase_1[corte]
    lista_aux = nova_frase_2.split(' ')
    b = lista_fav.append(lista_aux[0])
    tam_fav = len(lista_aux[0])
    novo_corte = 9 + tam_fav
    corte = slice(novo_corte, 34554)
    nova_frase_3 = nova_frase_2[corte]
    lista_aux = nova_frase_3.split(" ")
    c = lista_qtd.append(int(lista_aux[0]))
    return a, b, c

def captacao_info_2(lista_principal, frase_1):
    corte = slice(3, 34554)
    nova_frase_1 = frase_1[corte]
    lista_aux = nova_frase_1.split(' ')
    lista_principal.append(lista_aux[0])
    tam_nome = len(lista_aux[0])
    novo_corte = 26 + tam_nome
    corte = slice(novo_corte, 34554)
    nova_frase_2 = nova_frase_1[corte]
    lista_aux = nova_frase_2.split(' ')
    tam_tempo = len(lista_aux[0])
    lista_principal.append(int(lista_aux[0]))
    novo_corte = 12 + tam_tempo
    corte = slice(novo_corte, 34554)
    nova_frase_3 = nova_frase_2[corte]
    lista_aux = nova_frase_3.split(" ")
    tam_passos = len(lista_aux[0])
    lista_principal.append(int(lista_aux[0]))
    novo_corte = 35 + tam_passos
    corte = slice(novo_corte, 34554)
    nome_participante = nova_frase_3[corte]
    lista_principal.append(nome_participante)
    a = lista_principal
    return a

lista_nome = []
lista_fav = []
lista_qtd = []

n_participantes = int(input())

for i in range(n_participantes):
    apresentacao = input()
    captacao_info(lista_nome, lista_fav, lista_qtd, apresentacao)



print(lista_nome)
print(lista_fav)
print(lista_qtd)