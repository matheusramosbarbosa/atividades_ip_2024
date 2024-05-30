# Atividade 6-2 da Lista 2

# Importação de biblioteca exigida pelo desafio
from decimal import Decimal, getcontext

# Configuração de limite de 15 casas decimais
getcontext().prec = 15

# Inputs exigidos pelo desafio + variáveis de apoio
quantidade_veiculos = int(input())
acidente_info = input()
distancia_total = Decimal(input())
codigo_serializacao = input()
codigo_final = ""

# Cálculos do primeiro trajeto
trajeto_1 = "A"
distancia_jato = distancia_total * Decimal('0.8')
tempo_jato = (distancia_jato / Decimal('1089')) * Decimal('60')
distancia_carro = distancia_total * Decimal('0.2')
tempo_carro = (distancia_carro / Decimal('60')) * Decimal('60')
tempo_total_1 = tempo_carro + tempo_jato  # sem atrasos ainda

# Cálculos do segundo trajeto
trajeto_2 = "B"
distancia_onibus = distancia_total
tempo_onibus = (distancia_onibus / Decimal('40')) * Decimal('60')
tempo_total_2 = tempo_onibus  # sem atrasos ainda

# Cálculos do terceiro trajeto
trajeto_3 = "C"
distancia_helicoptero = distancia_total
tempo_helicoptero = ((distancia_helicoptero * Decimal('10')) / Decimal('60')) * Decimal('5')
tempo_total_3 = tempo_helicoptero

# Condição para definir adição de atraso no trânsito levando em consideração a quantidade de carros
if quantidade_veiculos > 0:
    tempo_total_1 += quantidade_veiculos * Decimal('0.6')
    tempo_total_2 += quantidade_veiculos * Decimal('0.6')

# Condição para definir adição de atraso no trânsito levando em consideração a existência de algum acidente
if acidente_info == "sim":
    tempo_total_1 += Decimal('20.0')
    tempo_total_2 += Decimal('20.0')

# Variáveis para organização do código
tempo_trajeto_1 = tempo_total_1
tempo_trajeto_2 = tempo_total_2
tempo_trajeto_3 = tempo_total_3

# Loop para criação do código de serialização
for i in codigo_serializacao:
    i = int(i)
    if i % 2 == 0:
        codigo_final += str(i) + "23"
    else:
        codigo_final += str(i) + "78"

# Outputs finais
print("Análise das opções de transporte até o show!")
print(f"Opção {trajeto_1} - Você chegará ao show em {tempo_trajeto_1:.1f} minutos")
print(f"Opção {trajeto_2} - Você chegará ao show em {tempo_trajeto_2:.1f} minutos")
print(f"Opção {trajeto_3} - Você chegará ao show em {tempo_trajeto_3:.1f} minutos")
print(f"---")
print(f"Senha de serialização transformada: {codigo_final}, guarde com segurança!")