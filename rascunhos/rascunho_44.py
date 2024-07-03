# Definindo as constantes e inicializando as variáveis
linhas = 5
colunas = 6
lim_box = 30

# Inicializa a primeira matriz (box) vazia
def criar_box_vazia():
    box = []
    for i in range(linhas):
        linha = []
        for a in range(colunas):
            linha.append('0')
        box.append(linha)
    return box

lista_matrizes = [criar_box_vazia()]

# Função para imprimir as boxes
def imprimir_boxes(lista_matrizes):
    for idx in range(len(lista_matrizes)):
        box = lista_matrizes[idx]
        print(f"BOX {idx + 1}:")
        for linha in box:
            print(" ".join(linha))
        print()  # Linha vazia após cada box

# Função para contar pokémons em uma box
def contar_pokemons(box):
    total = 0
    for linha in box:
        for pokemon in linha:
            if pokemon == '1':
                total += 1
    return total

# Função para capturar pokémons
def capturar(lista_matrizes, quantidade):
    while quantidade > 0:
        # Conta o número de pokémons na última box
        pokemons_na_ultima_box = contar_pokemons(lista_matrizes[-1])
        
        # Se a última box está cheia, cria uma nova box
        if pokemons_na_ultima_box == lim_box:
            lista_matrizes.append(criar_box_vazia())
        
        # Adiciona o Pokémon na última box disponível
        i = 0
        while i < linhas and quantidade > 0:
            a = 0
            while a < colunas and quantidade > 0:
                if lista_matrizes[-1][i][a] == '0':
                    lista_matrizes[-1][i][a] = '1'
                    quantidade -= 1
                a += 1
            i += 1
    
    imprimir_boxes(lista_matrizes)

# Função para transferir pokémons
def transferir(lista_matrizes, quantidade):
    while quantidade > 0 and len(lista_matrizes) > 0:
        i = linhas - 1
        while i >= 0 and quantidade > 0:
            a = colunas - 1
            while a >= 0 and quantidade > 0:
                if lista_matrizes[-1][i][a] == '1':
                    lista_matrizes[-1][i][a] = '0'
                    quantidade -= 1
                a -= 1
            i -= 1
        
        # Verifica se a última box está vazia
        box_vazia = True
        for i in range(linhas):
            for a in range(colunas):
                if lista_matrizes[-1][i][a] == '1':
                    box_vazia = False
        
        if box_vazia and len(lista_matrizes) > 1:
            lista_matrizes.pop()
    
    imprimir_boxes(lista_matrizes)

# Entrada inicial de pokémons armazenados
pokemons_armazenados = int(input("Digite o número de pokémons armazenados inicialmente: "))

# Captura os pokémons iniciais
if pokemons_armazenados > 0:
    capturar(lista_matrizes, pokemons_armazenados)

# Loop para receber os comandos
comando = input("Digite o comando (Capturar, Transferir ou Finalizar): ").strip()
while comando != "Finalizar":
    partes = comando.split()
    acao = partes[0]
    quantidade = int(partes[1])
    
    if acao == "Capturar":
        capturar(lista_matrizes, quantidade)
    elif acao == "Transferir":
        transferir(lista_matrizes, quantidade)

    comando = input("Digite o comando (Capturar, Transferir ou Finalizar): ").strip()

# Relatório final
print("RELATÓRIO FINAL:\n")
print(f"BOXES: {len(lista_matrizes)}")

# Conta o total de pokémons
pokemons_totais = 0
for box in lista_matrizes:
    for linha in box:
        for pokemon in linha:
            pokemons_totais += int(pokemon)

print(f"POKEMONS: {pokemons_totais}")
