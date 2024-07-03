# funções de cada operação
def adição(status_pokemon, valor_item):
  return status_pokemon + valor_item

def subtração(status_pokemon, valor_item):
  return status_pokemon - valor_item
  
def multiplicação(status_pokemon, valor_item):
  return status_pokemon * valor_item

def divisão(status_pokemon, valor_item):
  if valor_item == 0:
    return 0 # para n ter problema com divisão por 0 
  else:
    return status_pokemon / valor_item

def potenciação(status_pokemon, valor_item):
  return status_pokemon ** valor_item

def radiciação(status_pokemon, valor_item):
  if valor_item == 0:
    return 0 # para n ter problema radiciação com 0
  else:
    return int(status_pokemon ** (1 / valor_item))

# função que define os tipos de ações
def operações(ação, status_pokemon, valor_item):
  if ação == "Quero deixar meu Pokemon mais forte!":
    return adição(status_pokemon, valor_item), "Adição"
  elif ação == "Deixa eu testar esse cogumelo estranho…":
    return subtração(status_pokemon, valor_item), "Subtração"
  elif ação == "Vou evoluir meu Pokemon!":
    return multiplicação(status_pokemon, valor_item), "Multiplicação"
  elif ação == "Não! Essa comida diminui o ataque…":
    return divisão(status_pokemon, valor_item), "Divisão"
  elif ação == "E se eu colocar essa Mega Stone…":
    return potenciação(status_pokemon, valor_item), "Potenciação"
  elif ação == "Essa Mega Stone está estranha…":
    return radiciação(status_pokemon, valor_item), "Radiciação"
  else:
    return status_pokemon, "Operação desconhecida"
  
#inputs
quantidade_operações = int(input())

if quantidade_operações == -1:
  print("Acho que vou desistir, confio no meu Pokemon sem nenhum item!")
else:
  while quantidade_operações != 0: #loop para quantidade_operações
    ação = input()
    status_pokemon = int(input())
    valor_item = int(input())
    
    novo_status, nome_operacao = operações(ação, status_pokemon, valor_item)
    
    print(f"Ao dar esse item eu esperava uma operação de {nome_operacao} e com isso o status do meu Pokemon de {status_pokemon} foi para {novo_status}")

    quantidade_operações -= 1 
    
  print("Agora tenho confiança que vou vencer!")