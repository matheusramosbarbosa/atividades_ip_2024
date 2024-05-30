#Atividade 5 da Lista 2

# Variáveis de apoio
urna = True
total = 0
votos_kanye = 0
votos_outros = 0

# Loop para definir se a votação ainda está ativa
while urna:
    # Condição para definir se o bloco deverá permanecer ativo
    if total >= 300000000:
        urna = False
    else:
        # Se sim, então: Input exigidos pelo desafio
        bloco = input()

    # Condição para definir se o bloco desativará ou continuará
    if bloco == "FIM" and urna:
        urna = False
    elif bloco != "FIM" and urna:
        # Transforma str em int
        bloco = int(bloco)
        # Condição para definir contagem de votos
        if (bloco % 7 == 0) and (bloco % 2 != 0):
            votos_kanye += 20000000
            total += 20000000
        elif (bloco % 2 == 0) and (bloco % 7 != 0):
            votos_kanye += 10000000
            total += 10000000
        elif (bloco % 2 != 0) and (bloco % 7 != 0):
            votos_outros += 14000000
            total += 14000000

# Condição para output final
if votos_kanye > 170000000:
    print("O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    print(f'Kanye conseguiu ao final da campanha um total de {votos_kanye} votos.')
elif votos_kanye < 130000000:
    print("Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
    print(f'Kanye conseguiu ao final da campanha um total de {votos_kanye} votos.')
# Condição para caso os votos sejam maiores ou iguais a 130M e menores ou iguais a 170M, entrar no Segundo Turno
elif votos_kanye >= 130000000 and votos_kanye <= 170000000:
    # Entrada do Segundo Turno
    print(f'A eleição está disputada, vamos ter um segundo turno!')
    print(f'Kanye conseguiu ao final da campanha um total de {votos_kanye} votos.')
    # Abaixo mesma sintaxe do começo do programa, pois entra em um SEGUNDO TURNO
    urna = True
    total = 0
    votos_kanye = 0
    votos_outros = 0
    while urna:
        if total >= 300000000:
            urna = False
        else:
            bloco = input()

        if bloco == "FIM" and urna:
            urna = False
        elif bloco != "FIM" and urna:
            bloco = int(bloco)
            if (bloco % 7 == 0) and (bloco % 2 != 0):
                votos_kanye += 20000000
                total += 20000000
            elif (bloco % 2 == 0) and (bloco % 7 != 0):
                votos_kanye += 10000000
                total += 10000000
            elif (bloco % 2 != 0) and (bloco % 7 != 0):
                votos_outros += 14000000
                total += 14000000
    
    # Outputs finais
    if votos_kanye > 170000000:
        print("Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    else:
        print("Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")

    print(f'Kanye conseguiu ao final da campanha um total de {votos_kanye} votos.')