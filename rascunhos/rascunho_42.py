# texto = "DEFGHIJKLMNOPQRSTUVWXYZABC"
# lista = []
# for i in texto:
#     lista.append(i)

# print(lista)

# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# cifra = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C']
# cifra_traduzida = []

# def conversao_cifra(a):
#     for i in range(a, a + 26, 1):
#         caractere = alfabeto[i % len(alfabeto)]
#         cifra_traduzida.append(caractere)
#     b = cifra_traduzida
#     return b

# for j in range(3, 3 + 26, 1):
#     elemento = alfabeto[j % len(alfabeto)]
#     cifra_traduzida.append(elemento)

# cifrao = conversao_cifra(3)
# print(cifrao)

# nome = "Thomaz"
# nome = nome.lower()
# novo_nome = ''

# for i in nome:
#     aux_index = alfabeto.index(i)
#     novo_nome += cifra[aux_index]

# print(novo_nome)

# lista_numeros = []
# for i in range (97, 123):
#     lista_numeros.append(i)

# print(lista_numeros)

# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# valor_ascii = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

# def descobrir_id_jogador(a, b):
#     for i in a:
#         id_jogador = 0
#         for j in i:
#             index_aux = alfabeto.index(j)
#             id_jogador += valor_ascii[index_aux]
#         b.append(id_jogador)
#     return b

# lista_nomes = ["Matheus", "Henrique", "Ramos", "Barbosa"]

# nomes_lower = []
# for i in range (len(lista_nomes)):
#     nomes_lower.append(lista_nomes[i].lower())

# lista_aux = []
# lista_id_jogador = descobrir_id_jogador(nomes_lower, lista_aux)

# print(lista_id_jogador)

# numero = "738"

# for i in numero:
#     print(i)

lista = [['pipipi', 'popopo', 'papapa'], []]
frase_aux = ", ".join(lista[0])
print(frase_aux)