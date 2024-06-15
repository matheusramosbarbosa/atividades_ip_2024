# Atividade 2 da Lista 4
def imprimir(a, b, c):
    print(f'Ao dar esse item eu esperava uma operação de {a} e com isso o status do meu Pokemon de {b} foi para {c}')

def adicao(a, b):
    c = 0
    c = a + b
    return c

def subtracao(a, b):
    c = 0
    c = a - b
    return c

def multiplicacao(a, b):
    c = 0
    c = a * b
    return c

def divisao(a, b):
    c = 0
    c = a // b
    return c

def potenciacao(a, b):
    c = 0
    c = a**b
    return c

def radiciacao(a, b, c=0.000000001):
    # Método de Newton-Rapshon
    # Valor inicial do método:
    diferenca = 0
    aproximacao = 0
    melhor_aproximacao = 0
    aproximacao = a / 2.0
    diferenca = float("inf")
    while diferenca >= c:
        melhor_aproximacao = ((b - 1) * aproximacao + a / (aproximacao ** (b - 1))) / b
        diferenca = melhor_aproximacao - aproximacao
        if diferenca < 0:
            diferenca = -diferenca
        aproximacao = melhor_aproximacao
    parte_inteira = int(melhor_aproximacao)
    parte_decimal = melhor_aproximacao - parte_inteira
    if parte_decimal >= 0.5:
        return parte_inteira + 1
    else:
        return parte_inteira
    
operacao = True

while operacao:
    quantidade_operacoes = int(input())
    if quantidade_operacoes == -1:
        print(f'Acho que vou desistir, confio no meu Pokemon sem nenhum item!')
        operacao = False
    else:
        for i in range(quantidade_operacoes):
            acao = input()
            status_pokemon = int(input())
            valor_item = int(input())
            if acao == "Quero deixar meu Pokemon mais forte!":
                resultado_final = adicao(status_pokemon, valor_item)
                imprimir("Adição", status_pokemon, resultado_final)
            elif acao == "Deixa eu testar esse cogumelo estranho…":
                resultado_final = subtracao(status_pokemon, valor_item)
                imprimir("Subtração", status_pokemon, resultado_final)
            elif acao == "Vou evoluir meu Pokemon!":
                resultado_final = multiplicacao(status_pokemon, valor_item)
                imprimir("Multiplicação", status_pokemon, resultado_final)
            elif acao == "Não! Essa comida diminui o ataque…":
                resultado_final = divisao(status_pokemon, valor_item)
                imprimir("Divisão", status_pokemon, resultado_final)
            elif acao == "E se eu colocar essa Mega Stone…":
                resultado_final = potenciacao(status_pokemon, valor_item)
                imprimir("Potenciação", status_pokemon, resultado_final)
            elif acao == "Essa Mega Stone está estranha…":
                resultado_final = radiciacao(status_pokemon, valor_item)
                imprimir("Radiciação", status_pokemon, resultado_final)
        print(f'Agora tenho confiança que vou vencer!')
        operacao = False