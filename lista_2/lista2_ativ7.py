# Atividade 7 da Lista 2

# Input exigido pelo desafio + variáveis de apoio
quantidade_alunos = int(input())
votos_beyonce = 0
votos_taylor = 0
voto_novo = ""

# Loop para definir voto e qual aluno votou em quem com base na quantidade de alunos
for i in range (quantidade_alunos):
    # Input exigido pelo desafio
    voto = input()
    # Condição para atribuir votos às cantoras
    if voto == "beyonce":
        print(f"Aluno {i + 1} votou na Beyoncé.")
        votos_beyonce += 1
    elif voto == "taylor swift":
        print(f"Aluno {i + 1} votou na Taylor Swift.")
        votos_taylor += 1

# Outputs exigidos pela questão
print("Contagem de votos:")
print(f"Taylor Swift: {votos_taylor} votos")
print(f"Beyoncé: {votos_beyonce} votos")

# Condição para definir se deverá ser feito outro debate (caso os votos empatem)
if votos_taylor == votos_beyonce:
    print("Empate! Iniciando rodada de debate.")
    print("Alunos, agora é a sua chance de convencer os outros a mudar de voto!")
    for x in range (quantidade_alunos):
        quer_trocar = input()
        if quer_trocar == "sim":
            voto_novo = input()
            if voto_novo == "beyonce":
                print(f"Aluno {x + 1} mudou seu voto para Beyoncé.")
                votos_beyonce += 1
            elif voto_novo == "taylor swift":
                print(f"Aluno {x + 1} mudou seu voto para Taylor Swift.")
                votos_taylor += 1
        else:
            print(f"Aluno {x + 1} não mudou seu voto.")
    print("Nova contagem de votos após o debate:")
    print(f"Taylor Swift: {votos_taylor} votos")
    print(f"Beyoncé: {votos_beyonce} votos")

    # Condição para definir o voto de Aldo, presidente do evento, caso ainda empate no segundo debate
    if votos_taylor == votos_beyonce:
        print("Aldo, como presidente do evento, tem o voto decisivo.")
        voto_decisivo = input()

# Condição para output final
if votos_beyonce > votos_taylor:
    print(f"Beyoncé venceu com {votos_beyonce} votos! Será que Kanye West estava certo?")
elif votos_taylor > votos_beyonce:
    print(f"Taylor Swift venceu com {votos_taylor} votos! Kanye West tá irritado com isso.")
elif voto_decisivo == "beyonce":
    print("Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?")
elif voto_decisivo == "taylor swift":
    print("Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.")

