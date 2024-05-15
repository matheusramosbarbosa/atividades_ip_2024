import random

for i in range(10):
  x = random.randint(-10, 10)
  # evita a divisão por zero
  if x == 0:
    continue
  print(1/x)
