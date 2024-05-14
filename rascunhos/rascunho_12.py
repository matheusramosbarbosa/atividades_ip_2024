# Chegou a época de migração. Animais de diferentes tamanhos caminham entre duas localizações geográficas. Ambientalistas precisam calcular o esforço feito por cada animal durante a migração.

# Seu programa vai ler:

# nome do animal
# distância a ser percorrida (valor inteiro, em cm)
# tamanho do passo do animal (valor inteiro, em cm)
# No final, imprime uma mensagem, informando quantos passos o animal precisará dar para chegar ao destino.

# Use o comando for para calcular o número de passos.

# Dica: utilize a função range

# range(start, stop, step)

# start - início da sequência (opcional; default -> 0)
# stop - último elemento da sequência (obrigatório)
# step - intervalo entre os elementos (opcional; default -> 1)

nome = input()
distancia = int(input())
tam_passo = int(input())
resultado = 0

for i in range (1, distancia, tam_passo):
    resultado += 1
else:
    print(f'Cada {nome} precisará dar {resultado} passos.')
    