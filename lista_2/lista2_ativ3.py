# Atividade 3 da Lista 2

# Input exigido pelo desafio
qtd_praticas = int(input())

#Variáveis de apoio
pontuacao_final = 0
media = 0

# Textos armazenados em variáveis para evitar erros nas sintaxes das condições
# Boas práticas
boa_pratica_1 = "Programar utilizando uma boa IDE" # 3 pontos
boa_pratica_2 = "Códigos limpos e organizados" # 10 pontos
boa_pratica_3 = "Nomenclatura objetiva e de fácil identificação de variáveis" # 7 pontos
boa_pratica_4 = "Assistir às aulas do REDU" # 10 pontos
boa_pratica_5 = "Comentários significativos" # 5 pontos
boa_pratica_6 = "Evitar repetições desnecessárias de códigos" # 5 pontos
boa_pratica_7 = "Tirar dúvidas com os monitores e professores" # 10 pontos

# Más práticas
ma_pratica_1 = "Programar sem utilizar IDE" # -5 pontos
ma_pratica_2 = "Código bagunçado e mal estruturado" # -6 pontos
ma_pratica_3 = "Nomenclatura confusa e difícil de identificar variáveis" # -5 pontos
ma_pratica_4 = "Não tirar dúvidas com professores e monitores" # -10 pontos

# Loop FOR para receber cada resposta, de acordo com a quantidade de práticas submetidas pelo usuário
for i in range (qtd_praticas):
    pratica = input()
    if pratica == boa_pratica_1:
        pontuacao_final += 3
    elif pratica == boa_pratica_2:
        pontuacao_final += 10
    elif pratica == boa_pratica_3:
        pontuacao_final += 7
    elif pratica == boa_pratica_4:
        pontuacao_final += 10
    elif pratica == boa_pratica_5:
        pontuacao_final += 5
    elif pratica == boa_pratica_6:
        pontuacao_final += 5
    elif pratica == boa_pratica_7:
        pontuacao_final += 10
    elif pratica == ma_pratica_1:
        pontuacao_final -= 5
    elif pratica == ma_pratica_2:
        pontuacao_final -= 6
    elif pratica == ma_pratica_3:
        pontuacao_final -= 5
    elif pratica == ma_pratica_4:
        pontuacao_final -= 10

# Cálculo da média aritmética final, considerando a quantidade de práticas igual ou diferente de 0
if qtd_praticas == 0:
    media = 0
else:
    media = pontuacao_final / qtd_praticas

# Condições de arredondamento da média
if pontuacao_final < 0:
    media = 0
elif media > 10:
    media = 10

# Condições para definir o output final
if media < 3:
    print('É melhor voltar a cantar mesmo!')
elif media >= 3 and media < 7:
    print('Vai precisar se esforçar um pouco mais, meu cantor!')
elif media == 7:
    print('Na conta certa!')
elif media > 7 and media <= 9:
    print('Nasceu para programar!')
elif media > 9:
    print('Já pode ser chamado de Kanye, the dev, West!')