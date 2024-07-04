def contem_substring(principal, substring):
    # caso base se a substring tiver vazia
    if not substring:
        return True
    # caso base se a string principal for menor que a substring, então ela não pode conter a substring
    if len(principal) < len(substring):
        return False
    # verifica se a substring é igual ao início da string principal
    if principal.startswith(substring):
        return True
    # verfica o resto da string principal
    return contem_substring(principal[1:], substring)

def analise_de_palavra(principal, palavras, aux=0):
    # caso base se todas as palavras forem verificadas
    if aux == len(palavras):
        return True
    # analisa se a palavra atual existe na string principal
    if contem_substring(principal, palavras[aux]):
        return analise_de_palavra(principal, palavras, aux + 1)
    # se a palavra não estiver na string, retorna false
    return False

# input exigido pelo desafio
senha = input()

# lista que vai armazenar frases
frases = []

recebimento = True
while recebimento:
    frase = input()
    if frase == "Decifra-me ou te devoro!":
        recebimento = False
    else:
        frases.append(frase)

# analise de cada frase
senha_encontrada = False
i = 0
while i < len(frases) and not senha_encontrada:
    frase = frases[i]
    palavras = frase.split()
    if analise_de_palavra(senha, palavras):
        # output exigido pelo desafio
        print(f"Já sei, a senha é a frase número {i + 1}")
        senha_encontrada = True
    i += 1

# output exigido pelo desafio
if not senha_encontrada:
    print("Pensou que me enganaria? A magia da recursão me disse que a senha não pode ser nenhuma dessas")