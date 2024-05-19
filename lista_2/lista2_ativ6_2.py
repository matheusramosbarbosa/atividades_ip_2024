# Atividade 6 da Lista 2

# Importação de biblioteca
from decimal import Decimal, getcontext
getcontext().prec = 15

# Inputs exigidos pelo desafio + variáveis de apoio
quantidade_veiculos = int(input())
acidente_info = input()
distancia_total = float(input())
codigo_serializacao = input()
codigo_final = ""


# Cálculos do primeiro trajeto
trajeto_1 = "A"
distancia_jato = distancia_total * Decimal(0.8)
tempo_jato_temp = (distancia_jato * Decimal(60)) / Decimal(1089)
tempo_jato = tempo_jato_temp
distancia_carro = distancia_total * Decimal(0.2)
tempo_carro_temp = (distancia_carro * Decimal(60)) / Decimal(60)
tempo_carro = tempo_carro_temp
tempo_total_1 = tempo_carro + tempo_jato #sem atrasos ainda

# Cálculos do segundo trajeto
trajeto_2 = "B"
distancia_onibus = distancia_total
tempo_onibus_temp = (distancia_onibus * Decimal(60)) / Decimal(40)
tempo_onibus = tempo_onibus_temp
tempo_total_2 = tempo_onibus #sem atrasos ainda

# Cálculos do terceiro trajeto
trajeto_3 = "C"
distancia_helicoptero = distancia_total
tempo_helicoptero_temp = ((distancia_helicoptero * Decimal(10)) / Decimal(60)) * Decimal(5)
tempo_helicoptero = tempo_helicoptero_temp
tempo_total_3 = tempo_helicoptero

# Tempo de atraso
for i in range (quantidade_veiculos):
    tempo_total_1 += Decimal(0.36)
    tempo_total_2 += Decimal(0.36)

if acidente_info == "sim":
    tempo_total_1 += Decimal(20.0)
    tempo_total_2 += Decimal(20.0)

tempo_trajeto_1 = Decimal(tempo_total_1 * Decimal(10)) / Decimal(10)
tempo_trajeto_2 = Decimal(tempo_total_2 * Decimal(10)) / Decimal(10)
tempo_trajeto_3 = Decimal(tempo_total_3 * Decimal(10)) / Decimal(10)

for i in (codigo_serializacao):
    i = int(i)
    if i % 2 == 0:
        codigo_final += str(i) + "23"
    else:
        codigo_final += str(i) + "78"

print("Análise das opções de transporte até o show!")
print(f"Opção {trajeto_1} - Você chegará ao show em {tempo_trajeto_1:.1f} minutos")
print(f"Opção {trajeto_2} - Você chegará ao show em {tempo_trajeto_2:.1f} minutos")
print(f"Opção {trajeto_3} - Você chegará ao show em {tempo_trajeto_3:.1f} minutos")
print(f"---")
print(f"Senha de serialização transformada: {codigo_final}, guarde com segurança!")
