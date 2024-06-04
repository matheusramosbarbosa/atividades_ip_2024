# Atividade 1 da Lista 3

# Input exigidos pelo desafio
num_animais = int(input())

# Variáveis de apoio
i = num_animais
lista = []

# Loop principal que recebe o comando (input) e interpreta de acordo com o tipo da ordem
# Se baseia na quantidade de animais definida acima
while i > 0:
    # Input para receber o comando
    comando = input()
    # Condição para definir o que vai ser feito de acordo com o comando dado
    # Se for registrar, vai receber o nome do animal e vai registrar na lista
    # Caso, ao rodar o loop novamente, o animal digitado já esteja na lista, vai só mandar uma mensagem
    if comando == "REGISTRA":
        animal = input()
        if animal in lista:
            print(f'{animal} já foi registrado antes!')
        elif animal not in lista:
            lista.append(animal)
            print(f'{animal} registrado com sucesso.')
            # Retira 1 da quantidade de vezes que o loop vai rodar
            i -= 1
    # Se for corrigir um animal, vai retirar o animal da última posição da lista
    elif comando == "CORRIGE":
        if len(lista) < 1:
            print('O catálogo ainda está vazio.')
        else:
            # Uso de pop() para retirar o elemento que estiver no final da lista
            correcao = lista.pop(-1)
            print('Último registro apagado com sucesso.')
            # Adiciona 1 na quantidade de vezes que o loop vai rodar
            i += 1
    # Caso reinicie, a lista de animais vai redefinir tudo e o loop vai reiniciar, redefinindo a quantidade de
    # vezes que o loop vai rodar
    elif comando == "REINICIA":
        print('Catálogo redefinido com sucesso.')
        lista = []
        i = num_animais

# Outputs exigidos pelo desafio
print(f'Todos os animais foram registrados!\n')
print(f'Catálogo de animais:')
for a in range(num_animais):
    print(f'{a + 1}º: {lista[a]}')