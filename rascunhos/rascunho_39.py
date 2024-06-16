# Teste de slicing nas strings

# a = "Texto, Matheus, Alô, Pedra, Eu tenho"
# corte = slice(0,5)
# print(a[corte])
# corte = slice(0,11)
# print(a[corte])
# corte = slice(0,17)
# print(a[corte])
# corte = slice(0,18)
# print(a[corte])
# virgula = False

lista_nome = []
lista_fav = []
lista_qtd = []
lista_principal = []

# n_participantes = int(input())

# for i in range(n_participantes):
#     frase_1 = input()
#     corte = slice(16, 34554)
#     nova_frase_1 = frase_1[corte]
#     lista_aux = nova_frase_1.split(',')
#     lista_nome.append(lista_aux[0])
#     tam_nome = len(lista_aux[0])
#     novo_corte = 26 + tam_nome
#     corte = slice(novo_corte, 34554)
#     nova_frase_2 = nova_frase_1[corte]
#     lista_aux = nova_frase_2.split(' ')
#     lista_fav.append(lista_aux[0])
#     tam_fav = len(lista_aux[0])
#     novo_corte = 9 + tam_fav
#     corte = slice(novo_corte, 34554)
#     nova_frase_3 = nova_frase_2[corte]
#     lista_aux = nova_frase_3.split(" ")
#     lista_qtd.append(int(lista_aux[0]))

# print(lista_nome)
# print(lista_fav)
# print(lista_qtd)

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

frase_1 = input()
captacao_info_2(lista_principal, frase_1)
print(lista_principal)