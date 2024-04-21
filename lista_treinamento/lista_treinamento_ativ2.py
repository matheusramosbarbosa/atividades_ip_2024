#fórmula D² = (X1 - X2)² + (Z1 - Z2)²
#Hogsmeade (X: 34, Y: 110, Z: 220)
#Kakariko (X: 0, Y: 64, Z: 0)
#Solitude (X: 140, Y: 200, Z: 456)

import math

x = float(input())
z = float(input())

hogsmeade_x = 34
hogsmeade_z = 220
kakariko_x = 0
kakariko_z = 0
solitude_x = 140
solitude_z = 456

distancia_hogsmeade = math.sqrt(((hogsmeade_x - x) * (hogsmeade_x - x)) + ((hogsmeade_z - z) * (hogsmeade_z - z)))
distancia_kakariko = math.sqrt(((kakariko_x - x) * (kakariko_x - x)) + ((kakariko_z - z) * (kakariko_z - z)))
distancia_solitude = math.sqrt(((solitude_x - x) * (solitude_x - x)) + ((solitude_z - z) * (solitude_z - z)))

print(f'Distancia para Hogsmeade: {distancia_hogsmeade:0.2f}')
print(f'Distancia para Kakariko: {distancia_kakariko:0.2f}')
print(f'Distancia para Solitude: {distancia_solitude:0.2f}')

#depois tentar fazer pelo método de newton raphson