# Aí me fudeu

lista = [8, 3, 9, 1, 2, 3]
i = len(lista)
a = i // 2
lista1 = lista[:a]
lista2 = lista[a:]
lista_mesmo = []
b = len(lista1)
for y in range (b):
    lista_soma = lista1[y] + lista2[y]
    lista_mesmo.append(lista_soma)
print(lista_mesmo)