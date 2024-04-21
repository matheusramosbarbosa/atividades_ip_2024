#Precisa pegar o valor mais próximo portanto que seja maior do que o que Tantan precisa, e não pode ter uma oferta com menos do que o que ele precisa

d = int(input())

arthur = 10
luiz = 30
pedro = 100

if d > pedro:
    print('Nenhum')
elif d <= pedro and  d > luiz:
    print('Pedro')
elif d <= luiz and d > arthur:
    print('Luiz')
elif d <= arthur:
    print('Arthur')

#não sei se essa é a forma mais prática, preciso pesquisar depois