# Atividade 2 da Lista 2

# Input exigido pelo desafio
pessoas_entrevistadas = int(input())

# Variáveis com os textos/respostas para evitar erros na sintaxe das condições
adorei = "Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!"
nao_gostei = "Não gostei. Muito sem graça, onde já se viu nome com duas letras?"
acostumando = "Ainda estou me acostumando. Não tenho uma opinião formada sobre isso."

# Variáveis de apoio para uso nas condições
aprovacao = 0
rejeicao = 0
abstencao = 0

# Loop para receber cada resposta e armazenar quais foram de aprovação, rejeição e abstenção
for i in range (pessoas_entrevistadas):
    resposta = input()
    if resposta == adorei:
        aprovacao += 1
    if resposta == nao_gostei:
        rejeicao += 1
    if resposta == acostumando:
        abstencao += 1

# Cálculo para definir as taxas de aprovação, rejeição e abstenção
taxa_aprovacao = (aprovacao / pessoas_entrevistadas) * 100
taxa_rejeicao = (rejeicao / pessoas_entrevistadas) * 100
taxa_abstencao = (abstencao / pessoas_entrevistadas) * 100

# Outputs finais com as taxas limitadas a 2 casas decimais, e condição para definir a frase final de acordo com as taxas de aprovação e rejeição 
print("A pesquisa terminou e os resultados foram os seguintes:")
print(f'Taxa de aprovação: {taxa_aprovacao:.2f}')
print(f'Taxa de rejeição: {taxa_rejeicao:.2f}')
print(f'Taxa de abstenção: {taxa_abstencao:.2f}')

if taxa_aprovacao > taxa_rejeicao:
    print("YES!!! Sabia que as pessoas gostariam!")
elif taxa_rejeicao > taxa_aprovacao:
    print("Ops... Por essa eu não esperava.")
elif taxa_aprovacao == taxa_rejeicao:
    print("Bom... Vou olhar para o copo meio cheio!")