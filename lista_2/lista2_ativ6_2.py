# Atividade 6 da Lista 2

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
distancia_jato = Decimal(distancia_total) * Decimal(0.8)
tempo_jato = Decimal((distancia_jato * 60)) / Decimal(1089)
distancia_carro = Decimal(distancia_total) * Decimal(0.2)
tempo_carro = Decimal((distancia_carro * 60)) / Decimal(60)
tempo_total_1 = Decimal(tempo_carro) + Decimal(tempo_jato) #sem atrasos ainda

# Cálculos do segundo trajeto
trajeto_2 = "B"
distancia_onibus = Decimal(distancia_total)
tempo_onibus = Decimal((distancia_onibus * 60)) / Decimal(40)
tempo_total_2 = Decimal(tempo_onibus) #sem atrasos ainda

# Cálculos do terceiro trajeto
trajeto_3 = "C"
distancia_helicoptero = Decimal(distancia_total)
tempo_helicoptero = Decimal(((distancia_helicoptero * 10)) / Decimal(60)) * Decimal(5)
tempo_total_3 = Decimal(tempo_helicoptero)

# Tempo de atraso
for i in range (quantidade_veiculos):
    tempo_total_1 += Decimal(0.36)
    tempo_total_2 += Decimal(0.36)

if acidente_info == "sim":
    tempo_total_1 += Decimal(20)
    tempo_total_2 += Decimal(20)

tempo_trajeto_1 = Decimal(int(tempo_total_1 * 10) / 10)
tempo_trajeto_2 = Decimal(int(tempo_total_2 * 10) / 10)
tempo_trajeto_3 = Decimal(int(tempo_total_3 * 10) / 10)

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
