abcd = zip(range(1,8), range(5,8), range (9, 15), range(16, 25))
print(list(abcd))

for i, j in zip([1, 2, 3], [5, 6, 7]): #aqui ele cria 3 tuplas: (1, 5), (2, 6) e (3, 7)
  print(i * j)
else:
  print("Fim!")

for i, j in zip(range(1,4), range(5,8)): #aqui ele cria as tuplas (1, 5), (2, 6), (3, 7)
  print(i * j)
else:
  print("Fim!")