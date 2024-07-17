# Atividade 3 da Lista 6

# Função para calcular a idade da cidade
def calcular_idade(ano_fundacao):
    return 2024 - ano_fundacao

# Função para calcular a pontuação
def calcular_pontuacao(idade, posicao, visualizacoes):
    if posicao == 1:
        return idade + visualizacoes
    elif posicao == 2:
        return (idade // 2) + visualizacoes
    elif posicao == 3:
        return (idade // 3) + visualizacoes

# Lista de artistas candidatos
candidatos = ["João Gomes", "Zé Vaqueiro", "Raphaela Santos", "Alceu Valença", "Priscila Senna"]

# Armazenamento de pontuações e músicas
pontuacoes = {artista: 0 for artista in candidatos}
musicas_populares = {artista: ("", 0) for artista in candidatos}

# Mensagens para cidades específicas
mensagens_cidades = {
    "Recife": "A veneza brasileira foi consultada nesta pesquisa!",
    "Olinda": "Uma honra ver que a primeira capital pernambucana foi consultada!",
    "Petrolina": "Ansioso para descobrir a opinião dos petrolinenses!"
}

# Leitura do número de cidades
n = int(input().strip())

# Dados de cada cidade
for i in range (n):
    cidade = input().strip()
    ano_fundacao = int(input().strip())
    idade = calcular_idade(ano_fundacao)

    # Loop para leitura dos artistas e suas músicas
    for posicao in range(1, 4):
        entrada = input().strip().split(" - ")
        artista = entrada[0]
        musica = entrada[1]
        visualizacoes = int(entrada[2])
        
        if artista in candidatos:
            pontuacao = calcular_pontuacao(idade, posicao, visualizacoes)
            pontuacoes[artista] += pontuacao
            
            if visualizacoes > musicas_populares[artista][1]:
                musicas_populares[artista] = (musica, visualizacoes)
    
    # Exibindo mensagem específica da cidade se tiver
    if cidade in mensagens_cidades:
        print(mensagens_cidades[cidade])

# Definição do vencedor
vencedor = max(pontuacoes, key=pontuacoes.get)
musica_vencedora, visualizacoes_vencedor = musicas_populares[vencedor]

# Outputs finais exigidos pelo desafio
mensagem_vencedor = {
    "João Gomes": "Parabéns, João Gomes, o novo fenômeno da música pernambucana!",
    "Zé Vaqueiro": "Zé Vaqueiro, o astro do forró, agora brilha como o rei da música pernambucana!",
    "Raphaela Santos": "Raphaela Santos, a voz marcante, agora é a rainha da música pernambucana!",
    "Alceu Valença": "Alceu Valença, o ícone da MPB, agora é o gigante da música pernambucana!",
    "Priscila Senna": "Priscila Senna, a rainha da sofrência, é a mais nova estrela da música pernambucana!"
}

print(mensagem_vencedor[vencedor])
print(f"O fenômeno é {vencedor}, que canta a música {musica_vencedora}, já contando com mais de {visualizacoes_vencedor} milhões de visualizações na internet.")
