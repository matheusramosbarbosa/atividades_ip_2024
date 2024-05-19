# Solicita a palavra secreta
palavra_secreta = input("Digite a palavra secreta: ")

# Inicializa a palavra oculta com sublinhados
palavra_oculta = ['_' for _ in palavra_secreta]

# Inicia o loop para os chutes
while '_' in palavra_oculta:
    # Mostra a palavra oculta atual
    for letra in palavra_oculta:
        print(letra, end="")
    print()
    
    # Solicita um chute do usuário
    chute = input("Digite uma letra: ")
    
    # Verifica se o chute está na palavra secreta
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == chute:
            palavra_oculta[i] = chute
    
    # Mostra a palavra oculta após o chute
    for letra in palavra_oculta:
        print(letra, end="")
    print()

print("Parabéns, você adivinhou a palavra:", palavra_secreta)