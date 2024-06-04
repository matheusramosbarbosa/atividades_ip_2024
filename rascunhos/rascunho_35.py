salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
salas_concluidas = ["caldeira", "aquário", "mural"]

copa_conjuntos = [
  ["Recursos da primavera", ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]],
  ["Recursos do Verão", ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]],
  ["Recursos do Outono", ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]],
  ["Recursos do Inverno", ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]]
]

artesanato_conjuntos = [
  ["Plantacoes da Primavera", ["chirivia", "vagem", "couve-flor", "batata"]],
  ["Plantacoes do Verão", ["tomate", "mirtilo", "melao", "pimenta-quente"]],
  ["Plantacoes do Outono", ["milho", "beringela", "abobora", "inhame"]],
  ["Artesão", ["mel", "geleia", "queijo", "tecido"]]
]

recursos_primavera = copa_conjuntos[0][1]
recursos_verao = copa_conjuntos[1][1]
recursos_outono = copa_conjuntos[2][1]
recursos_inverno = copa_conjuntos[3][1]

platacoes_primavera = artesanato_conjuntos[0][1]
plantacoes_verao = artesanato_conjuntos[1][1]
platacoes_outono = artesanato_conjuntos[2][1]
artesao = artesanato_conjuntos[3][1]

sala_desejada = input()
conjuntos_desejados = input().split(', ')
itens_bau = input().split(', ')

if sala_desejada in salas_concluidas:
  print(f"Eu já concluí {sala_desejada}, não precisa doar mais itens para essa sala")

elif sala_desejada not in salas:
  print("Essa sala não está no centro comunitário")

else:

  if " " in conjuntos_desejados or " " in itens_bau:
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
  else:
    itens_repetidos = []

    for item in itens_bau:
      item_pertence = False
      if sala_desejada == "copa":
        for conjunto in conjuntos_desejados:
          if conjunto == 'recursos da primavera' and item not in recursos_primavera:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
                      
          elif conjuntos_desejados == "recursos do verão" and item not in recursos_verao:
            print(f"{item} vai ser entregue ao centro logo!")
            item_pertence = True
              
          elif conjunto == "recursos do outono" and item not in recursos_outono:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
          
          elif conjunto == "recursos do inverno" and item not in recursos_inverno:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
                  
      elif sala_desejada == "artesanato":
        for conjunto in conjuntos_desejados:
          if conjunto == "Plantacoes da Primavera" and item not in platacoes_primavera:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
    
          elif conjunto == "Plantacoes do Verão" and item not in plantacoes_verao:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
        
          elif conjunto == "Plantacoes do Outono" and item not in platacoes_outono:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
        
          elif conjunto == "Artesão" and item not in artesao:
            print(f"{item} pode ser analisado depois")
            item_pertence = True
                    
      if not item_pertence and item not in itens_repetidos:
        print(f"{item} vai ser entregue ao centro logo!")

      if itens_bau.count(item) > 1 and item not in itens_repetidos:
        itens_repetidos.append(item)

    if itens_repetidos:
      print("Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…")