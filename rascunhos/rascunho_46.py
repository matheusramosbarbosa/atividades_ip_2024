def fatorial(n):
  if(n == 0):
    return 1
  else:
    return n * fatorial(n-1)

x = fatorial(4)
print(x)