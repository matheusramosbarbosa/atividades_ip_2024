# Atividade 1 da Lista 2

# Inputs exigidos pelo desafio
nome_ouvinte = input()
quantidade_musicas = int(input())
maior_musica = ""
menor_musica = ""
maior_streams = 0
menor_streams = 1000000000

# Loop FOR que termina quando repetir a quantidade de vezes da quantidade de músicas
for i in range (quantidade_musicas):
    musica = input()
    quantidade_streams = int(input())
    if quantidade_streams > maior_streams:
        maior_streams = quantidade_streams
        maior_musica = musica
    if quantidade_streams < menor_streams:
        menor_streams = quantidade_streams
        menor_musica = musica

# Condições para definir o output final
if quantidade_musicas == 0:
    print(f'{nome_ouvinte} é team Taylor e não ouviu Kanye West')
elif quantidade_musicas == 1:
    print(f'A única música que {nome_ouvinte} ouviu foi {musica} com {quantidade_streams} streams')
elif (quantidade_musicas > 1) and (maior_streams == menor_streams):
    print(f'A música que {nome_ouvinte} mais ouviu foi {maior_musica} com {maior_streams} streams')
elif quantidade_musicas > 1:
    print(f'A música que {nome_ouvinte} mais ouviu foi {maior_musica} com {maior_streams} streams')
    print(f'A música que {nome_ouvinte} menos ouviu foi {menor_musica} com {menor_streams} streams')