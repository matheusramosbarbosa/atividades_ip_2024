num = int(input('Digite um inteiro no intervalo [0-100]:'))

while((num<0) or (num>100)):
  print('Intervalo inválido!!!')
  num = int(input('Digite um inteiro no intervalo [0-100]:'))
  
# se for par, vai para o próximo número ímpar
if(num%2 == 0):
  num += 1

while(num<99):
  print(f'{num},', end=' ')
  num += 2
else:
  print (f'{num}.')
