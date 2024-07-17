# Atividade 2 da Lista 6

# Dados da semana 1
artistas_semana1 = {"Priscila Senna": {"discos": 40, "fortuna": 10000}, "Eduarda": {"discos": 60, "fortuna": 9990}, "Academia da Berlinda": {"discos": 30, "fortuna": 9995}, "Martins": {"discos": 25, "fortuna": 9970}, "Igor de Carvalho": {"discos": 25, "fortuna": 9965}}

# Função para calcular o lucro baseado na quantidade de discos vendidos
def calcular_lucro(discos):
    preco_unitario = 20
    if discos == 1:
        return discos * preco_unitario
    elif 2 <= discos <= 3:
        return discos * preco_unitario * 0.98
    elif 4 <= discos <= 5:
        return discos * preco_unitario * 0.95
    elif discos >= 6:
        return discos * preco_unitario * 0.93

# Leitura do input para a semana 2
n = int(input().strip())
artistas_semana2_list = [input().strip().split(" - ") for i in range(n)]
artistas_semana2 = dict((artista[0], int(artista[1])) for artista in artistas_semana2_list)

# Processamento dos dados para a semana 2
novos_artistas = {}
aumentos = {}
houve_aumento = False  # Flag para verificar se houve aumento de lucro

for artista, discos_vendidos in artistas_semana2.items():
    lucro = calcular_lucro(discos_vendidos)
    
    if artista in artistas_semana1:
        fortuna_antiga = artistas_semana1[artista]["fortuna"]
        nova_fortuna = fortuna_antiga + lucro
        aumento_percentual = ((nova_fortuna - fortuna_antiga) / fortuna_antiga) * 100
        artistas_semana1[artista]["fortuna"] = nova_fortuna
        aumentos[artista] = aumento_percentual
        if aumento_percentual > 0:
            houve_aumento = True
    else:
        novos_artistas[artista] = {"discos": discos_vendidos, "fortuna": lucro}
        artistas_semana1[artista] = {"discos": discos_vendidos, "fortuna": lucro}

aumentos_list = list(aumentos.items())
artistas_list = list(artistas_semana1.items())

# Verificando se houve aumento
if houve_aumento:
    print("Estes artistas obtiveram aumento do lucro em relação à primeira semana:")
    for artista, aumento in aumentos_list:
        if aumento > 0:
            print(f"{artista} - Lucro em relação à primeira semana: {aumento:.2f}%")
else:
    print("Os artistas da primeira semana não tiveram aumento do lucro na segunda semana!")

# Printando a fortuna atual dos artistas
print("\nEsta é a fortuna atual dos artistas considerados:")
for artista, dados in artistas_list:
    print(f"{artista}: R$ {dados['fortuna']:.2f}")

# Output final exigido pelo desafio
novos_artistas_list = list(novos_artistas.items())
if novos_artistas_list:
    print("\nNa semana 2 tivemos vendas de novos artistas no mercado:")
    for artista, dados in novos_artistas_list:
        print(f"{artista} - Discos vendidos: {dados['discos']}")
else:
    print("\nNa semana 2 não tivemos vendas de novos artistas no mercado!")
