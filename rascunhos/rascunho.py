
# x = float(input())
# z = float(input())

# hogsmeade_x = 34
# hogsmeade_z = 220
# kakariko_x = 0
# kakariko_z = 0
# solitude_x = 140
# solitude_z = 456

# distancia_hogsmeade = ((hogsmeade_x - x) * (hogsmeade_x - x)) + ((hogsmeade_z - z) * (hogsmeade_z - z))

# print(f'Distancia para Hogsmeade: {distancia_hogsmeade:0.2f}')

print('Vamos descobrir qual o maior valor entre dois números.')
a = int(input('Ponha o primeiro valor: '))
b = int(input('Ponha o segundo valor: '))

x = (a + b + (abs(a - b))) // 2
print(f'O maior valor é {x}')