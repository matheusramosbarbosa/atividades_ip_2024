#função len(texto) conta a quantidade de caracteres
n = input()
s = input()

qtd_caracteres = len(n + s)

if((qtd_caracteres > 3) and (qtd_caracteres < 16)):
    print(n + s)