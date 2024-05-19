# Atividade 7 da Lista 2

quantidade_alunos = int(input())
votos_beyonce = 0
votos_taylor = 0
voto_novo = ""

for i in range (quantidade_alunos):
    voto = input()
    if voto == "beyonce":
        print(f"Aluno {i} votou na Beyoncé.")
        votos_beyonce += 1
    elif voto == "taylor swift":
        print(f"Aluno {i} votou na Taylor Swift.")
        votos_taylor += 1

print("Contagem de votos:")
print(f"Taylor Swift: {votos_taylor} votos")
print(f"Beyoncé: {votos_beyonce} votos")

if votos_taylor == votos_beyonce:
    print("Empate! Iniciando rodada de debate.")
    print("Alunos, agora é a sua chance de convencer os outros a mudar de voto!")
    for x in range (quantidade_alunos):
        voto_novo = input()
        if voto_novo == "beyonce":
            print(f"Aluno {x} votou na Beyoncé.")
            votos_beyonce += 1
        elif voto_novo == "taylor swift":
            print(f"Aluno {x} votou na Taylor Swift.")
            votos_taylor += 1