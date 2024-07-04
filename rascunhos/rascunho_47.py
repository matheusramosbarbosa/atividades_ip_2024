# Atividades de recursão

'''
def soma_lista(lista):
    if(lista == []):
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
    

numeros = [1, 2, 3, 4, 5]

print(soma_lista(numeros))

'''


# def conta_elementos(lista):
#     if(lista == []):
#         return 0
#     else:
#         return 1 + conta_elementos(lista[1:])
    
# numeros = [1, 2, 3, 4, 5]
# print(conta_elementos(numeros))


# def inverte_string(s):
#     if(s == ''):
#         return ''
#     else:
#         return s[-1] + inverte_string(s[:-1])
    
# s = "recursão"
# print(inverte_string(s))  # Deve imprimir "oãsrucre"

# def soma_digitos(n):
#     if(n == 0):
#         return 0
#     else:
#         return n % 10 + soma_digitos(n // 10)
    
# n = 12345
# print(soma_digitos(n))  # Deve imprimir 15

# def conta_vogais(s):
#     if(s == ''):
#         return 0
#     else:
#         if (s[0].lower() in 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕ'):
#             return 1 + conta_vogais(s[1:])
#         else:
#             return conta_vogais(s[1:])

# s = "Recursão"
# print(conta_vogais(s))  # Deve imprimir 4

# def maior_elemento(lista, maior=0):
#     if(len(lista) == 1):
#         return lista[0]
#     else:
#         maior_dos_restantes = maior_elemento(lista[1:])
#         if lista[0] > maior_dos_restantes:
#             return lista[0]
#         else:
#             return maior_dos_restantes
        
# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(maior_elemento(numeros))  # Deve imprimir 9

# def potencia(x, n):
#     if(n == 0):
#         return 1
#     else:
#         return x * potencia(x, n-1)
    
# x = 2
# n = 3
# print(potencia(x, n))  # Deve imprimir 8


# def contem_substring(string_principal, substring):
#     # Caso base: se a substring estiver vazia, é trivialmente encontrada
#     if not substring:
#         return True
#     # Caso base: se a string_principal for menor que a substring, não pode conter a substring
#     if len(string_principal) < len(substring):
#         return False
#     # Verifica se a substring corresponde ao início da string_principal
#     if string_principal[:len(substring)] == substring:
#         return True
#     # Verifica recursivamente o restante da string_principal
#     return contem_substring(string_principal[1:], substring)

# def verifica_substrings(string_principal, substrings, index=0, resultados=None):
#     # Inicializa o dicionário de resultados na primeira chamada
#     if resultados is None:
#         resultados = {}
#     # Caso base: se o índice atingir o comprimento da lista de substrings, retorne os resultados
#     if index == len(substrings):
#         return resultados
#     # Adiciona o resultado da verificação atual ao dicionário
#     substring = substrings[index]
#     resultados[substring] = contem_substring(string_principal, substring)
#     # Chama recursivamente para o próximo índice
#     return verifica_substrings(string_principal, substrings, index + 1, resultados)

# # String principal
# string_principal = "jorkhij"

# # Substrings a verificar
# substrings = ["jo", "rk", "hij", "jork"]

# # Verificação usando a função recursiva
# resultados = verifica_substrings(string_principal, substrings)

# # Exibindo os resultados
# print(resultados)

def contem_substring(string_principal, substring):
    # Caso base: se a substring estiver vazia, é trivialmente encontrada
    if not substring:
        return True
    # Caso base: se a string_principal for menor que a substring, não pode conter a substring
    if len(string_principal) < len(substring):
        return False
    # Verifica se a substring corresponde ao início da string_principal
    if string_principal.startswith(substring):
        return True
    # Verifica recursivamente o restante da string_principal
    return contem_substring(string_principal[1:], substring)

def verifica_palavras_na_string(string_principal, palavras, index=0):
    # Caso base: se todas as palavras foram verificadas, retorna True
    if index == len(palavras):
        return True
    # Verifica se a palavra atual está contida na string_principal
    if contem_substring(string_principal, palavras[index]):
        # Verifica recursivamente para a próxima palavra
        return verifica_palavras_na_string(string_principal, palavras, index + 1)
    # Se qualquer palavra não estiver contida, retorna False
    return False

# Leitura da linha contínua do orc
linha_orc = input().strip().lower()

# Lista para armazenar as frases
frases = []

recebimento = True
while recebimento:
    frase = input().strip()
    if frase == "Decifra-me ou te devoro!":
        recebimento = False
    else:
        frases.append(frase.lower())

# Verificação de cada frase sem usar 'in'
senha_encontrada = False
i = 0
while i < len(frases) and not senha_encontrada:
    frase = frases[i]
    palavras = frase.split()
    if verifica_palavras_na_string(linha_orc, palavras):
        print(f"Já sei, a senha é a frase número {i + 1}")
        senha_encontrada = True
    i += 1

# Se nenhuma frase servir como senha
if not senha_encontrada:
    print("Pensou que me enganaria? A magia da recursão me disse que a senha não pode ser nenhuma dessas")

