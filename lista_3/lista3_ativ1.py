# Atividade 1 da Lista 3

num_animais = int(input())
i = num_animais
lista = []

while i > 0:
    comando = input()
    if comando == "REGISTRA":
        animal = input()
        if animal in lista:
            print(f'{animal} já foi registrado antes!')
        elif animal not in lista:
            lista.append(animal)
            print(f'{animal} registrado com sucesso.')
            i -= 1
    elif comando == "CORRIGE":
        if len(lista) < 1:
            print('O catálogo ainda está vazio.')
        else:
            correcao = lista.pop(-1)
            print('Último registro apagado com sucesso.')
            i += 1
    elif comando == "REINICIA":
        print('Catálogo redefinido com sucesso.')
        lista = []
        i = num_animais

print(f'Todos os animais foram registrados!\n')
print(f'Catálogo de animais:')
for a in range(num_animais):
    print(f'{a + 1}º: {lista[a]}')