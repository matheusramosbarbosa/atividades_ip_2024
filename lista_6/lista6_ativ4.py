# Atividade 4 da Lista 6

# Funções pra imprimir
def imprimir_boas_vindas():
    print("Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!")

def imprimir_artistas(artista1, artista2):
    print(f"E os artistas de hoje são {artista1} e {artista2}!")

def imprimir_comeco_expediente():
    print("-----COMEÇO DO EXPEDIENTE!-----")

def imprimir_fim_expediente():
    print("-----FIM DO EXPEDIENTE!-----")

def imprimir_disco_vendido(disco):
    print(f"{disco} vendido")

def imprimir_disco_nao_encontrado():
    print("Parece que não temos esse disco...")

def imprimir_ajuste_preco(artista_mais, artista_menos):
    print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista_mais.upper()} E ABAIXA R$4 DE {artista_menos.upper()}!")

def imprimir_receita_total(receita_total, discos_vendidos_total):
    print(f"O total de receita gerado foi de {receita_total} e foram vendidos {discos_vendidos_total} discos.")

def imprimir_sem_vendas():
    print("Que tristeza! Só artista péssimo...")

def imprimir_empate():
    print("Difícil de escolher o melhor!")

def imprimir_vencedor(artista, receita, discos_vendidos):
    print(f"O artista que mais gerou dinheiro para a loja foi {artista}, acumulando uma receita de {receita} e vendendo {discos_vendidos} discos.")

# Principal
imprimir_boas_vindas()

artista1 = input().strip()
artista2 = input().strip()

imprimir_artistas(artista1, artista2)

# Leitura de discos e preços
discos_artistas = {artista1: {}, artista2: {}}
precos_artistas = {artista1: {}, artista2: {}}

for artista in [artista1, artista2]:
    lendo_discos = True
    while lendo_discos:
        nome_disco = input().strip()
        if nome_disco == "acabou":
            lendo_discos = False
        else:
            preco_disco = float(input().strip())
            discos_artistas[artista][nome_disco] = 0  # Contagem de vendas
            precos_artistas[artista][nome_disco] = preco_disco  # Preço

imprimir_comeco_expediente()

# Vendas
receita_total = 0
discos_vendidos_total = 0
vendas_artistas = {artista1: 0, artista2: 0}
receita_artistas = {artista1: 0.0, artista2: 0.0}

vendendo_discos = True
while vendendo_discos:
    disco_vendido = input().strip()
    if disco_vendido == "FIM":
        vendendo_discos = False
    else:
        disco_encontrado = False
        for artista in [artista1, artista2]:
            if disco_vendido in discos_artistas[artista]:
                disco_encontrado = True
                discos_artistas[artista][disco_vendido] += 1
                vendas_artistas[artista] += 1
                preco_venda = precos_artistas[artista][disco_vendido]
                receita_artistas[artista] += preco_venda
                receita_total += preco_venda
                discos_vendidos_total += 1
                imprimir_disco_vendido(disco_vendido)

                # Verificação de condição
                diferenca_vendas = vendas_artistas[artista1] - vendas_artistas[artista2]
                if diferenca_vendas >= 3 and diferenca_vendas % 3 == 0:
                    artista_mais, artista_menos = artista1, artista2
                elif diferenca_vendas <= -3 and (-diferenca_vendas) % 3 == 0:
                    artista_mais, artista_menos = artista2, artista1
                else:
                    artista_mais, artista_menos = None, None

                if artista_mais and artista_menos:
                    for disco in precos_artistas[artista_mais]:
                        precos_artistas[artista_mais][disco] += 4

                    for disco in precos_artistas[artista_menos]:
                        precos_artistas[artista_menos][disco] = max(1.0, precos_artistas[artista_menos][disco] - 4)

                    imprimir_ajuste_preco(artista_mais, artista_menos)

        if not disco_encontrado:
            imprimir_disco_nao_encontrado()

imprimir_fim_expediente()

# Print de receita total
if receita_total == int(receita_total):
    receita_total = float(receita_total)
else:
    receita_total = round(receita_total, 1)

imprimir_receita_total(receita_total, discos_vendidos_total)

# Output exigido pelo desafio
if vendas_artistas[artista1] == 0 and vendas_artistas[artista2] == 0:
    imprimir_sem_vendas()
elif receita_artistas[artista1] == receita_artistas[artista2]:
    imprimir_empate()
else:
    if receita_artistas[artista1] > receita_artistas[artista2]:
        vencedor = artista1
    else:
        vencedor = artista2

    imprimir_vencedor(vencedor, round(receita_artistas[vencedor], 1), vendas_artistas[vencedor])
