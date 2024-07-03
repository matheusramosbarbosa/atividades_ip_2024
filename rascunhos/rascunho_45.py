# Teste

lista_matheus = []
lista_skug = []
gosto = 0

matheus = True
while matheus:
    personagens_matheus = input()
    if personagens_matheus == "Finalizar":
        matheus = False
    else:
        lista_math_aux = personagens_matheus.split(". ", 1)
        personagem_atual = lista_math_aux[1]
        lista_matheus.append(personagem_atual)

skug = True
while skug:
    personagens_skug = input()
    if personagens_skug == "Finalizar":
        skug = False
    else:
        lista_skug_aux = personagens_skug.split(". ", 1)
        personagem_atual = lista_skug_aux[1]
        lista_skug.append(personagem_atual)


posicoes = []
personagens_posicoes = []
for i in range(len(lista_matheus)):
    if lista_matheus[i] == lista_skug[i]:
        gosto += 1
        posicoes.append(str(i + 1))
        personagens_posicoes.append(lista_matheus[i])

lista_gosto = []
for i in range(len(personagens_posicoes)):
    lista_gosto.append(f'{posicoes[i]}° - {personagens_posicoes[i]}')

porcentagem = (gosto * 100) / len(lista_matheus)

print(f'Matheus e Skug! Vamos aos resultados...')
print(f'O gosto de vocês é... {porcentagem:.1f}% parecido!')
print(f'E vocês concordaram com os personagens nessas posições:')
for i in lista_gosto:
    print(i)