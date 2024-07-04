def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def n_th_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def possiveis_armas(vida_boss, armas):
    tipos_armas = [n_th_prime(i + 1) for i in range(len(armas))]
    possiveis = [(armas[i], tipos_armas[i]) for i in range(len(armas)) if vida_boss % tipos_armas[i] == 0]
    return possiveis

def simula_turno(vida_boss, jogadores, index=0, armas_usadas=set()):
    if vida_boss <= 0:
        return 0
    if index == len(jogadores):
        return 0
    
    jogador_armas = jogadores[index]
    possiveis = possiveis_armas(vida_boss, jogador_armas)
    dano_maximo = 0

    for arma, tipo_arma in possiveis:
        if tipo_arma not in armas_usadas:
            novas_armas_usadas = armas_usadas.copy()
            novas_armas_usadas.add(tipo_arma)
            dano = arma + simula_turno(vida_boss - arma, jogadores, index + 1, novas_armas_usadas)
            dano_maximo = max(dano_maximo, dano)
    
    dano_sem_arma = simula_turno(vida_boss, jogadores, index + 1, armas_usadas)
    dano_maximo = max(dano_maximo, dano_sem_arma)
    
    return dano_maximo

def calcula_dano_maximo(vida_boss, jogadores):
    return simula_turno(vida_boss, jogadores)

# Leitura da entrada
N = int(input().strip())
jogadores = []
for _ in range(N):
    armas = list(map(int, input().strip().split()))
    jogadores.append(armas)
vida_boss = int(input().strip())

# Calculo do dano máximo
dano_maximo = calcula_dano_maximo(vida_boss, jogadores)

# Verificação do resultado
if dano_maximo >= vida_boss:
    print("Felizmente conseguimos vencer!")
else:
    print("Infelizmente nao conseguiremos vencer dessa vez.")
print(f"Dano maximo: {dano_maximo}")
