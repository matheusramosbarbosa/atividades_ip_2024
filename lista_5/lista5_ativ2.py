# Atividade 2 da Lista 5

def mdc(x, y):
    if(y == 0):
        return x
    else:
        return mdc(y, x % y) 
    
pares = int(input())
lista_pares = []
senha_final = 0

for i in range(pares):
    par = input()
    par = par.split(" ")
    for a in range(len(par)):
        par[a] = int(par[a])

    if par[0] > par[1]:
        maior = par[0]
        menor = par[1]
    else:
        maior = par[1]
        menor = par[0]

    x = mdc(maior, menor)
    print(f'O MDC entre {par[0]} e {par[1]} é {x}')
    senha_final += x

print()    
print(f'A senha final foi {senha_final}')

