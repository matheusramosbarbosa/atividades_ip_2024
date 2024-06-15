nomes_tipos = [["Misty", "Gary", "Ivy", "Blanche"], ["Ash", "Ritchie", "Surge", "Spark"], ["May", "Blaine", "Candela"], ["Agatha", "Sabrina", "Fantina"], ["Jessie", "James", "Giovanni"], ["Lorelei", "Dawn"], ["Max", "Erika", "Tracey", "Mallow"], ["Whitney"]]
especies = ["Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Glaceon", "Leafeon", "Sylveon"]

nome_selecionado = input()

for i in nomes_tipos:
    if nome_selecionado in i:
        tipo = i

aux_index = nomes_tipos.index(tipo)
print(aux_index)