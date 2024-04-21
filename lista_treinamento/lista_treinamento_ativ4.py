#meu deus esse aqui eh punk

a = int(input()) #quantidade de diamantes por hora
l = int(input()) #quantidade de diamantes por hora
p = int(input()) #quantidade de diamantes por hora
h = int(input()) #quantidade de horas

x = (a + l + (abs(a - l))) // 2 #função/equação para descobrir maior número entre dois 
y = x
z = (x + p + (abs(x - p))) // 2
m = z * h #maior numero de de diamantes por hora vezes quantidade de horas

print(f'{m}')








# print('Vamos descobrir qual o maior valor entre dois números.')
# a = int(input('Ponha o primeiro valor: '))
# b = int(input('Ponha o segundo valor: '))

# x = (a + b + (abs(a - b))) // 2
# print(f'O maior valor é {x}')
