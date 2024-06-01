# lista = ['Matheus', 'João', 'Ricardo', 'Gustavo', 'Bituco']
# print(lista)

# indice_atual = int(input())
# indice_novo = int(input())
# lista.insert(indice_novo, lista[indice_atual])
# auxiliar2 = lista.pop(4)
# print(lista)

lista = ['Matheus', 'João', 'Ricardo', 'Gustavo', 'Bituco']
print(lista)

indice_atual = int(input())
indice_novo = int(input())
auxiliar2 = lista.pop(indice_atual)
lista.insert(indice_novo, auxiliar2)
print(lista)