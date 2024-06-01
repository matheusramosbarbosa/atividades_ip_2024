num_animais = int(input())
i = num_animais
lista = []

for i in range(num_animais):
    comando = input()
    if comando == "REGISTRA":
        animal = input()
        while animal in lista:
            print(f'{animal} já foi registrado antes!')
            animal = input()
        if animal not in lista:
            lista.append(animal)
            print(f'{animal} registrado com sucesso!')
    elif comando == "CORRIGE":
        if len(lista) < 1:
            print('O catálogo está vazio')
        else:
            correcao = lista.pop(-1)
        i += 1
    elif comando == "REINICIA":
        print('Catálogo redefinido com sucesso.')
        lista = []
        i = num_animais

print(f'Todos os animais foram registrados!\n')
print(f'Catálogo de animais:')
for a in range(num_animais):
    print(f'{a + 1}º: {lista[a]}')