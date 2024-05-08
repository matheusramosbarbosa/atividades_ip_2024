from random import radint #random é a biblioteca e radint é a função importada da biblioteca

# gera número inteiro aleatório entre 0 e 100
num = radint(0, 100)
num

num_escolhido = int(input("Escolha um número"))
while (num_escolhido != num):
  if num_escolhido > num:
    print("O numero sorteado é menor!")
    num_escolhido = int(input("Escolha um número"))
  elif (num_escolhido < num):
    print("O número sorteado é maior!")
    num_escolhido = int(input("Escolha um número"))
else:
  print("Parabéns! Você acertou o número!")